# Meu Conversor de Currículo HTML para PDF 🚀

Olá! Bem-vindo(a) ao repositório do meu projeto de Conversor de Currículo HTML para PDF. Esta é uma ferramenta que desenvolvi para facilitar a vida de quem, assim como eu, gosta de criar currículos personalizados em HTML mas enfrenta dificuldades na hora de convertê-los para PDF com fidelidade visual.

![image](https://github.com/user-attachments/assets/5e8bdc7f-05cc-48f7-9aee-baa671d9c864)

## A Ideia 💡

Tudo começou com uma frustração pessoal: eu criava currículos visualmente atraentes em HTML, mas, ao tentar usar a função "Imprimir para PDF" (Ctrl+P) dos navegadores, a formatação frequentemente quebrava – layouts desconfigurados, fontes diferentes, cores sumindo e conteúdo cortado eram problemas comuns. Eu queria uma maneira de garantir que o PDF final fosse um reflexo exato do meu design HTML. Assim, decidi construir este sistema!

## Sobre o Projeto 📄

Este é um aplicativo web local, desenvolvido com **Python** e o framework **Django**, que utiliza o poder do **Playwright** para realizar a mágica da conversão. Ele permite que você faça o upload do seu arquivo `index.html` e o converta para um arquivo PDF com qualidade.

**Status Atual:** A ferramenta já está funcional para a conversão de HTML para PDF! No entanto, como todo projeto em desenvolvimento, ainda há alguns ajustes e melhorias que pretendo implementar com o tempo.

## Tecnologias Utilizadas 🛠️

* **Python 3.13+**
* **Django 5.x:** Para a estrutura web e backend.
* **Playwright:** Para automação de navegador e a renderização fiel do HTML.
* **HTML5, CSS3:** Para a interface da própria ferramenta.

## Funcionalidades Atuais ✨

* Upload de arquivo `index.html`.
* Definição do nome do arquivo de saída pelo usuário.
* Conversão do HTML para o formato **PDF** (configurado para A4).
* Download direto do arquivo PDF gerado.

## Como Rodar o Projeto Localmente (Instalação) ⚙️

Para rodar este projeto na sua máquina local (Windows 11 testado), siga os passos:

1.  **Clone o Repositório (ou Baixe os Arquivos):**
    ```bash
    git clone https://github.com/DevDevanir/Conversor_de_Curriculo.git
    cd nome-do-diretorio-do-projeto
    ```

2.  **Crie e Ative um Ambiente Virtual Python:**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    # source venv/bin/activate
    ```

![image](https://github.com/user-attachments/assets/8d2fbdfe-6406-48c5-827f-9218e582a585)


3.  **Instale as Dependências:**
    Certifique-se de ter o arquivo `requirements.txt` no seu projeto e rode:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Instale os Navegadores do Playwright:**
    Este comando baixa os navegadores headless que o Playwright utiliza.
    ```bash
    playwright install
    ```

5.  **Aplique as Migrações do Django:**
    ```bash
    python manage.py migrate
    ```

6.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

![image](https://github.com/user-attachments/assets/b4c954f5-ebbb-4138-80a8-65e4e768df91)


7.  Acesse a aplicação no seu navegador em: `http://127.0.0.1:8000/`

![image](https://github.com/user-attachments/assets/8116ac31-19d6-45eb-9586-7348c7390d79)


## Como Utilizar a Ferramenta 📋

Após iniciar o servidor local:

1.  Abra seu navegador e acesse `http://127.0.0.1:8000/`.
2.  Você verá a interface "Conversor de Currículo HTML".
3.  Clique em "Escolher arquivo" e selecione o arquivo `index.html` do seu currículo.
    * _Observação importante:_ No momento, o sistema processa melhor HTMLs que são auto-contidos (CSS e JS embutidos) ou que utilizam recursos online (CDNs para fontes, imagens hospedadas). Se o seu HTML depende de arquivos CSS, JS ou imagens locais com caminhos relativos, eles podem não ser carregados corretamente na conversão, pois o sistema atualmente só faz upload do `index.html`.
4.  No campo "Nome do arquivo de saída (sem extensão)", digite o nome que deseja para o seu PDF (Ex: `meu_curriculo_versao_final`). Evite espaços e caracteres especiais; use letras, números, `_` ou `-`.
5.  A opção "PDF" já estará selecionada como formato de saída.
6.  Clique no botão "Converter e Baixar".
7.  Seu navegador iniciará o download do arquivo PDF gerado!

## Processo de Desenvolvimento e Auxílio 🧠

O desenvolvimento desta ferramenta foi uma grande jornada de aprendizado. Durante todo o processo, desde a concepção da ideia até a implementação e os testes, contei com o valioso **auxílio de uma Inteligência Artificial (IA) da Google**.

A IA foi fundamental em diversas etapas:
* **Planejamento:** Ajudou a definir a arquitetura do sistema e a escolher as tecnologias mais adequadas (como Django para o backend e Playwright para a conversão fiel do HTML).
* **Estruturação do Código:** Forneceu a estrutura inicial para os arquivos do projeto Django (`settings.py`, `urls.py`, `views.py`, `forms.py`, templates HTML, etc.).
* **Lógica de Programação:** Auxiliou na escrita da lógica de upload de arquivos, na integração com o Playwright para a conversão e na lógica para servir o arquivo gerado para download.
* **Depuração de Erros:** Foi uma grande aliada na identificação e correção de bugs e erros que surgiram.
* **Explicação de Conceitos:** Ajudou a entender melhor o funcionamento do Django, a manipulação de formulários, a API do Playwright e as melhores práticas de desenvolvimento.
* **Criação de Documentação:** Inclusive, auxiliou na elaboração deste `README` e de outros textos explicativos.

Sem dúvida, a colaboração com a IA acelerou o desenvolvimento e enriqueceu meu aprendizado!

## Próximos Passos e Visão de Futuro 🔮

Esta ferramenta já é funcional, mas tenho planos para continuar aprimorando-a:

* [ ] **Ajuste Fino na Renderização:** Investigar e corrigir o problema de espaçamento excessivo na parte inferior de alguns PDFs convertidos, para garantir que a captura da página seja mais precisa em relação à altura real do conteúdo.
* [ ] **Melhorias na Interface do Usuário (UI/UX):** Tornar a interface mais intuitiva e com um design mais elaborado.
* [ ] **Suporte a Upload de Pacotes .ZIP:** Permitir o upload de um arquivo .zip contendo o `index.html` e todos os seus assets locais (CSS, JS, imagens, fontes) para garantir que os caminhos relativos funcionem perfeitamente.
* [ ] **Reintroduzir Opções de Imagem (PNG/JPEG):** Adicionar novamente a funcionalidade de converter para formatos de imagem, com mais controle sobre dimensões e qualidade.
* [ ] **Opções Avançadas de PDF:** Permitir configurar margens, orientação, etc.
* [ ] **Limpeza Automática de Arquivos:** Implementar um sistema mais robusto para limpar arquivos temporários do servidor.

E a grande visão para o futuro:
> Conforme eu for tendo tempo, irei aperfeiçoando essa ferramenta. A intenção é que ela faça no futuro **currículos personalizados com o uso de inteligência artificial**, talvez ajudando a gerar conteúdo ou adaptar layouts dinamicamente!

## Contribuições e Feedback ❤️

Este é um projeto pessoal, mas se você tiver ideias, sugestões de melhoria ou encontrar algum bug, sinta-se à vontade para abrir uma *Issue* neste repositório (se aplicável). Todo feedback construtivo é bem-vindo!

---

Obrigado por conferir o projeto!
