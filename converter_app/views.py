# Este arquivo contém a lógica (views) para o aplicativo converter_app.
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponseServerError, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import uuid # Para gerar nomes de arquivo únicos
from playwright.sync_api import sync_playwright # Importa o Playwright

from .forms import UploadFileForm # Importa nosso formulário

def converter_view(request):
    """
    View para lidar com o upload do arquivo HTML, conversão e download.
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            html_file = request.FILES['html_file']
            output_filename_user = form.cleaned_data['output_filename']
            output_format = form.cleaned_data['output_format']

            # Validação simples do nome do arquivo (pode ser melhorada)
            if not output_filename_user.isalnum() and '_' not in output_filename_user and '-' not in output_filename_user:
                # Adiciona uma mensagem de erro se o nome do arquivo for inválido
                # (Idealmente, isso seria tratado na validação do formulário)
                form.add_error('output_filename', 'Nome do arquivo de saída contém caracteres inválidos.')
                return render(request, 'converter_app/index.html', {'form': form, 'error_message': 'Nome do arquivo de saída contém caracteres inválidos.'})


            # Salvar o arquivo HTML enviado temporariamente
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
            # Gera um nome de arquivo único para evitar sobrescrever arquivos com o mesmo nome
            unique_id = uuid.uuid4().hex[:8] # Pega os primeiros 8 caracteres do UUID
            temp_filename = f"{unique_id}_{html_file.name}"
            uploaded_file_path = fs.save(temp_filename, html_file)
            full_uploaded_file_path = fs.path(uploaded_file_path) # Caminho absoluto

            # Definir o nome do arquivo de saída e o caminho
            output_file_basename = f"{output_filename_user}_{unique_id}.{output_format}"
            converted_file_dir = os.path.join(settings.MEDIA_ROOT, 'converted_files')
            os.makedirs(converted_file_dir, exist_ok=True) # Cria o diretório se não existir
            converted_file_path = os.path.join(converted_file_dir, output_file_basename)

            try:
                with sync_playwright() as p:
                    # Tenta usar o Chromium primeiro, depois Firefox, depois Webkit
                    # Isso aumenta a robustez caso um navegador não esteja disponível
                    # ou tenha problemas com um HTML específico.
                    browser_types = [p.chromium, p.firefox, p.webkit] 
                    page = None

                    for browser_type in browser_types:
                        try:
                            browser = browser_type.launch()
                            context = browser.new_context(
                                # Define uma viewport grande para tentar capturar tudo,
                                # mas para PDF o 'format' A4 é mais importante.
                                # Para imagens, full_page=True é o principal.
                                viewport={'width': 1920, 'height': 10800}, # Altura bem grande
                                device_scale_factor=2 # Aumenta a resolução da imagem (DPI)
                            )
                            page = context.new_page()
                            # Navega para o arquivo HTML local usando o protocolo file://
                            page.goto(f"file://{full_uploaded_file_path}")
                            
                            # Espera um pouco para garantir que tudo carregue (se houver JS complexo)
                            # Para HTMLs simples, isso pode não ser necessário.
                            page.wait_for_timeout(1000) # 1 segundo

                            break # Sai do loop se o navegador for iniciado com sucesso
                        except Exception as e_browser:
                            print(f"Erro ao iniciar {browser_type.name}: {e_browser}")
                            if browser_type == browser_types[-1]: # Se foi o último navegador tentado
                                raise # Re-levanta a exceção se todos falharem
                            # Tenta o próximo navegador
                    
                    if not page: # Se nenhum navegador pôde ser iniciado
                         return HttpResponseServerError("Erro: Não foi possível iniciar um navegador para conversão.")

                    if output_format == 'pdf':
                        page.pdf(path=converted_file_path, format='A4', print_background=True)
                    elif output_format == 'png':
                        page.screenshot(path=converted_file_path, full_page=True, type='png')
                    elif output_format == 'jpeg':
                        page.screenshot(path=converted_file_path, full_page=True, type='jpeg', quality=90) # Qualidade para JPEG
                    
                    browser.close()

                # Oferecer o arquivo para download
                # FileResponse lida com o tipo MIME correto automaticamente
                response = FileResponse(open(converted_file_path, 'rb'), as_attachment=True, filename=output_file_basename)
                
                # Limpeza (opcional, mas recomendado para arquivos temporários)
                # Você pode querer deletar os arquivos após o download ou após um certo tempo.
                # fs.delete(uploaded_file_path) # Deleta o HTML enviado
                # os.remove(converted_file_path) # Deleta o arquivo convertido após o download (cuidado com isso)
                # Para uma limpeza mais robusta, considere tarefas agendadas (Celery) ou políticas de retenção.

                return response

            except Exception as e:
                print(f"Erro durante a conversão: {e}")
                # Limpa o arquivo enviado se a conversão falhar
                if fs.exists(uploaded_file_path):
                    fs.delete(uploaded_file_path)
                # Retorna uma mensagem de erro para o usuário
                return render(request, 'converter_app/index.html', {'form': form, 'error_message': f"Ocorreu um erro durante a conversão: {e}"})
            finally:
                # Garante que o arquivo HTML enviado seja deletado mesmo se ocorrer um erro
                # após a conversão mas antes do FileResponse, ou se o usuário cancelar o download.
                # No entanto, deletar aqui pode ser problemático se o FileResponse ainda estiver usando o arquivo.
                # Uma estratégia melhor é limpar arquivos antigos periodicamente.
                # Por simplicidade, vamos deletar apenas o arquivo de upload aqui se ele ainda existir
                # e a conversão não foi bem sucedida (ou seja, não retornou o FileResponse).
                # A limpeza do arquivo convertido é mais complexa de gerenciar de forma síncrona.
                pass # A limpeza foi comentada acima para evitar problemas com FileResponse

        else: # Se o formulário não for válido
            return render(request, 'converter_app/index.html', {'form': form})
    else: # Se for um request GET (primeira vez que acessa a página)
        form = UploadFileForm()
    
    return render(request, 'converter_app/index.html', {'form': form})


