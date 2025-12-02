# DeepCode (Ambiente Local)

"Onde agentes de IA transformam ideias em código pronto para produção" — Ambiente Windows com servidor Streamlit em `http://localhost:8510`.

## Visão Geral
- Interface web moderna para orquestrar agentes e implementar código a partir de requisitos (Text2Web/Text2Backend/Paper2Code).
- Arquitetura baseada em agentes MCP (Model Context Protocol), com integração a ferramentas e provedores de LLM.
- Fluxos principais: análise, planejamento, criação de estrutura, implementação de código e indexação de referências.

## Requisitos
- Windows 10/11
- Python 3.11–3.13 (recomendado 3.13)
- Git
- Navegador moderno

## Instalação (local)
1. Clone o repositório:
   - `git clone https://github.com/fabiorjvr/DEEPCODE.git`
   - `cd DEEPCODE`
2. Crie e ative o ambiente virtual:
   - `python -m venv venv`
   - `venv\Scripts\activate`
3. Instale dependências (se necessário, ajuste conforme seu ambiente):
   - `pip install streamlit`
   - Instale servidores MCP se for utilizar busca, filesystem, etc.
4. Configure chaves de API em `mcp_agent.secrets.yaml` (NUNCA comite chaves reais):
   - `anthropic.api_key: YOUR_ANTHROPIC_API_KEY`
   - `openai.api_key: YOUR_OPENAI_API_KEY`
   - `google.api_key: YOUR_GOOGLE_API_KEY`
   - `groq.api_key: YOUR_GROQ_API_KEY`
5. Se preferir, use `Install-DeepCode.ps1` para automação básica de instalação no Windows.

## Execução
- Via script (recomendado):
  - Crie um atalho para o script de inicialização e execute.
  - Ou execute diretamente: `INICIAR_DEEPCODE_CORRIGIDO.bat` (local).
- Via Python/Streamlit (equivalente):
  - `venv\Scripts\python.exe -m streamlit run venv\Lib\site-packages\ui\streamlit_app.py --server.port 8510 --server.address localhost`
- Acesse `http://localhost:8510`.

## Configuração
- `mcp_agent.config.yaml`: modelos e provedores; utiliza placeholders por padrão.
- `mcp_agent.secrets.yaml`: chaves reais (local, fora do controle de versão).
- `mcp_config_completo.yaml`: configuração estendida; mantenha placeholders no repositório.
- Boas práticas: nunca comitar segredos; utilize variáveis de ambiente ou arquivos locais ignorados.

## Arquitetura de Workflows
- `workflows/agent_orchestration_engine.py`: orquestra análise, planejamento e execução.
- `workflows/code_implementation_workflow.py`: implementação padrão (sem índice de referências).
- `workflows/code_implementation_workflow_index.py`: implementação com indexador.
- Prompts em `prompts/code_prompts.py`: contém `STRUCTURE_GENERATOR_PROMPT` e system prompts.

## Segurança e Segredos
- Push Protection do GitHub bloqueia segredos (ex.: chaves Groq/Google). Mantemos placeholders no repositório.
- Armazene chaves em `mcp_agent.secrets.yaml` localmente (ignoradas pelo `.gitignore`) ou como variáveis de ambiente.

## Boas Práticas de Git/GitHub
- Branches:
  - `main`: estável
  - `feature/<tema>`: novas funcionalidades
  - `fix/<bug>`: correções
  - `chore/<tarefa>`: manutenção
- Commits:
  - Mensagens curtas e objetivas, prefixos como `feat:`, `fix:`, `docs:`, `chore:`
  - Exemplos: `docs: adiciona README detalhado`, `chore: remove arquivos desnecessários`
- Pull Requests:
  - Descreva objetivo, mudanças, verificação e impacto
  - Link para issues quando aplicável
- `.gitignore`:
  - Ignora `venv/`, caches e artefatos locais
  - Nunca versionar chaves/segredos

## Solução de Problemas
- ImportError de prompts: garantir `prompts/code_prompts.py` com constantes requeridas.
- Tipos Python 3.13: use `typing.Union/Optional` para compatibilidade com versões e pydantic v2.
- Erros de segredos ao realizar push: substitua por placeholders e faça `commit --amend` antes de `git push`.

## Roadmap (sugestões)
- Adicionar testes automatizados
- Fornecer script de inicialização multiplataforma
- Documentar integrações MCP adicionais

## Licença
- Defina uma licença conforme sua preferência (por exemplo, MIT). Caso deseje, posso adicionar o arquivo `LICENSE`.

