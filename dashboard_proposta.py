import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import datetime

# Verifica se o Graphviz está instalado
try:
    import graphviz
    graphviz_installed = True
except ImportError:
    graphviz_installed = False

# =============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Proposta de Transformação Digital - Scrum",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# 2. CSS CUSTOMIZADO
# =============================================================================
custom_css = """
<style>
body {
    font-family: 'Roboto', sans-serif;
    background-color: #f4f4f8;
    color: #000000 !important;
    margin: 0;
    padding: 0;
}
.block-container {
    background-color: #fff;
    border-radius: 12px;
    padding: 2rem 3rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
h1, h2, h3 {
    color: #283c63;
}
h1 {
    font-size: 2.5rem;
}
h2 {
    font-size: 2rem;
}
.stExpander {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 1rem;
}
.stProgress > div > div > div > div {
    background-image: linear-gradient(to right, #4facfe, #00f2fe);
}
.sprint-task {
    background-color: #e9ecef;
    padding: 0.75rem;
    border-radius: 6px;
    margin-bottom: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.goal-target {
    background-color: #f9f9f9;
    padding: 0.75rem;
    border-radius: 6px;
    margin-bottom: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.streamlit-expanderHeader {
    font-size: 1.2rem;
    color: #3366cc;
    font-weight: bold;
}
.highlight {
    font-weight: bold;
    color: #007bff;
}
.company-container {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    background-color: #f9f9f9;
}
.sprint-details {
    margin-top: 1rem;
    padding: 0.5rem;
    border: 1px solid #eee;
    border-radius: 4px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# 3. CABEÇALHO
# =============================================================================
st.title("Proposta de Transformação Digital - Scrum")
st.subheader("Estratégias Personalizadas para Crescimento Acelerado")
st.caption("Liderança: Alberth (Head de Dados, Tecnologia e Marketing com IA)")
st.caption("Product Owner: Ricardo Menendez Sarmento")
st.write("---")

# =============================================================================
# 4. VISÃO GERAL DO PROJETO
# =============================================================================
st.subheader("Visão Geral Estratégica (4 Meses)")
st.write("""
Este projeto visa integrar automações, desenvolver sistemas customizados e aplicar análises de dados avançadas para aprimorar o desempenho organizacional.  
Sob a liderança de **Alberth** e com o gerenciamento do backlog por **Ricardo**, adotaremos a metodologia **Scrum** para garantir entregas de alto valor em sprints de 2 semanas.  
Cada ciclo contará com Daily Stand-ups, Sprint Reviews e Retrospectivas, assegurando melhoria contínua e adaptação às necessidades dos *stakeholders*.
""")
st.write("---")

# =============================================================================
# 5. ROADMAP DE IMPLEMENTAÇÃO
# =============================================================================
st.subheader("Roadmap de Implementação")
roadmap_data = {
    "Mês 1": {"progresso": 30, "objetivo": "Definição do Escopo e Planejamento Inicial", 
              "meta": "Escopo detalhado e backlog priorizado.", 
              "descricao": "Estabelecimento das bases do projeto com reuniões iniciais e definição das prioridades."},
    "Mês 2": {"progresso": 55, "objetivo": "Desenvolvimento e Implementação Base", 
              "meta": "Protótipos funcionais e integração inicial.", 
              "descricao": "Desenvolvimento dos primeiros módulos e integração das soluções básicas."},
    "Mês 3": {"progresso": 80, "objetivo": "Otimização e Testes", 
              "meta": "Sistemas otimizados e testes validados.", 
              "descricao": "Execução de testes rigorosos e ajustes para garantir alta performance."},
    "Mês 4": {"progresso": 100, "objetivo": "Implantação e Melhorias Contínuas", 
              "meta": "Deploy final com monitoramento e ajustes pós-implementação.", 
              "descricao": "Lançamento das soluções e monitoramento contínuo para aperfeiçoamento."}
}
cols = st.columns(4)
for i, mes in enumerate(roadmap_data.keys()):
    with cols[i]:
        st.write(f"**{mes}**")
        st.progress(roadmap_data[mes]["progresso"] / 100)
        with st.expander(f"Detalhes de {mes}"):
            st.markdown(f"""
            <div class="goal-target">
                <strong>Objetivo:</strong> {roadmap_data[mes]["objetivo"]}
            </div>
            <div class="goal-target">
                <strong>Meta:</strong> {roadmap_data[mes]["meta"]}
            </div>
            <p>{roadmap_data[mes]["descricao"]}</p>
            """, unsafe_allow_html=True)
st.write("---")

# =============================================================================
# 6. PROJETOS E SPRINTS DEDICADAS
# =============================================================================
st.subheader("Projetos e Sprints Dedicadas")
companies = {
    "Fênix Telecom": {
        "description": "Soluções tecnológicas para automação.",
        "objective": "Integração de API, funil de vendas e automação de pedidos.",
        "sprints": {
            "Keilon": [
                {"sprint": 1, "task": "Criar endpoints de API para integração com sistemas legados", "hours": 20},
                {"sprint": 2, "task": "Garantir a segurança e escalabilidade das integrações", "hours": 15},
                {"sprint": 3, "task": "Realizar testes de carga e estresse", "hours": 20},
                {"sprint": 4, "task": "Implementar funil de vendas e automação de pedidos", "hours": 20}
            ],
            "Thiago": [
                {"sprint": 1, "task": "Análise de dados para otimização do funil", "hours": 15},
                {"sprint": 2, "task": "Implementação de painéis de monitoramento", "hours": 20},
                {"sprint": 3, "task": "Automação de relatórios de desempenho", "hours": 15}
            ],
            "Ricardo": [
                {"sprint": 1, "task": "Definir prioridades do backlog e alinhar requisitos", "hours": 10},
                {"sprint": 2, "task": "Revisar protótipos e validar entregas iniciais", "hours": 8}
            ],
            "Alberth": [
                {"sprint": 1, "task": "Estabelecer estratégia de integração e supervisão do projeto", "hours": 12},
                {"sprint": 3, "task": "Avaliar performance das integrações e ajustar roadmap estratégico", "hours": 10}
            ]
        },
    },
    "Chalés Recanto da Paz": {
        "description": "Insights de dados para decisões estratégicas.",
        "objective": "Pipelines de automação, relatórios avançados e funil de vendas PWA.",
        "sprints": {
            "Keilon": [
                {"sprint": 1, "task": "Desenvolver funil de vendas em PWA", "hours": 20},
                {"sprint": 2, "task": "Otimizar a experiência do usuário nas reservas", "hours": 15},
                {"sprint": 3, "task": "Integrar sistema de pagamento no PWA", "hours": 20}
            ],
            "Thiago": [
                {"sprint": 1, "task": "Coletar e estruturar dados para análise", "hours": 15},
                {"sprint": 2, "task": "Criar pipelines de automação no Maker.com", "hours": 20},
                {"sprint": 3, "task": "Gerar relatórios dinâmicos com métricas-chave", "hours": 15},
                {"sprint": 4, "task": "Análise preditiva de ocupação", "hours": 10}
            ],
            "Ricardo": [
                {"sprint": 1, "task": "Priorizar funil de vendas e requisitos para PWA", "hours": 10},
                {"sprint": 3, "task": "Validar relatórios e KPIs com feedback dos stakeholders", "hours": 8}
            ],
            "Alberth": [
                {"sprint": 1, "task": "Definir estratégia de insights e supervisão do pipeline", "hours": 12},
                {"sprint": 2, "task": "Monitorar implementação dos painéis e KPIs estratégicos", "hours": 10}
            ]
        },
    },
    "AGX Capital": {
        "description": "Agência de design especializada em visuais.",
        "objective": "Geração automatizada de arte e site com IA.",
        "sprints": {
            "Keilon": [
                {"sprint": 1, "task": "Desenvolver templates dinâmicos para artes", "hours": 20},
                {"sprint": 2, "task": "Integrar templates com ferramentas de design", "hours": 15},
                {"sprint": 3, "task": "Desenvolver site institucional e IA de atendimento", "hours": 20}
            ],
            "Thiago": [
                {"sprint": 1, "task": "Criar pipelines para alimentar templates com dados", "hours": 15},
                {"sprint": 2, "task": "Garantir alinhamento com diretrizes de branding", "hours": 20},
                {"sprint": 3, "task": "Implementar automação avançada no site", "hours": 15},
                {"sprint": 4, "task": "Realizar testes A/B para otimização de conversão", "hours": 10}
            ],
            "Ricardo": [
                {"sprint": 1, "task": "Revisar requisitos para templates e site institucional", "hours": 10},
                {"sprint": 3, "task": "Validar funcionalidades e performance da IA", "hours": 8}
            ],
            "Alberth": [
                {"sprint": 1, "task": "Supervisionar integração de ferramentas de design", "hours": 12},
                {"sprint": 2, "task": "Acompanhar implantação de automação avançada e estratégia de marca", "hours": 10}
            ]
        },
    },
    "Brprix Transportes": {
        "description": "Solução de transporte e logística.",
        "objective": "Monitoramento de motoristas e funil de vendas automatizado.",
        "sprints": {
            "Keilon": [
                {"sprint": 1, "task": "Implementar sistema de monitoramento GPS", "hours": 20},
                {"sprint": 2, "task": "Integrar WhatsApp para automação de vendas", "hours": 15},
                {"sprint": 3, "task": "Desenvolver sistema de alertas", "hours": 20}
            ],
            "Thiago": [
                {"sprint": 1, "task": "Configurar infraestrutura de dados", "hours": 15},
                {"sprint": 2, "task": "Analisar rotas para otimização de custos", "hours": 20},
                {"sprint": 3, "task": "Criar painel de controle para gestão da frota", "hours": 15},
                {"sprint": 4, "task": "Implementar sistema de segurança com alertas preditivos", "hours": 10}
            ],
            "Ricardo": [
                {"sprint": 1, "task": "Priorizar funcionalidades do sistema de monitoramento", "hours": 10},
                {"sprint": 3, "task": "Validar integração do WhatsApp com funil de vendas", "hours": 8}
            ],
            "Alberth": [
                {"sprint": 1, "task": "Definir estratégia de monitoramento e campanhas de tráfego", "hours": 12},
                {"sprint": 2, "task": "Supervisionar análise de rotas e otimização logística", "hours": 10}
            ]
        },
    },
    "DHE Componentes Hidráulicos": {
        "description": "Componentes hidráulicos e serviços.",
        "objective": "Site de vendas de serviços e funil de vendas automatizado.",
        "sprints": {
            "Keilon": [
                {"sprint": 1, "task": "Arquitetura do site de serviços", "hours": 20},
                {"sprint": 2, "task": "Design do formulário de captura de leads", "hours": 15},
                {"sprint": 3, "task": "Integração do chatbot para atendimento", "hours": 20}
            ],
            "Thiago": [
                {"sprint": 1, "task": "Definir estratégia de conteúdo para o site", "hours": 15},
                {"sprint": 2, "task": "Teste e implementação do chatbot", "hours": 20},
                {"sprint": 3, "task": "Analisar resultados e propor melhorias contínuas", "hours": 15},
                {"sprint": 4, "task": "Implementar análise de dados para otimizar o funil", "hours": 10}
            ],
            "Ricardo": [
                {"sprint": 1, "task": "Alinhar requisitos para site e funil automatizado", "hours": 10},
                {"sprint": 3, "task": "Revisar integração do chatbot e performance do funil", "hours": 8}
            ],
            "Alberth": [
                {"sprint": 1, "task": "Estabelecer estratégia de integração de APIs", "hours": 12},
                {"sprint": 2, "task": "Monitorar testes e validação do sistema", "hours": 10}
            ]
        },
    },
}

for company, details in companies.items():
    with st.expander(f"**{company}**", expanded=False):
        st.markdown(f"**Descrição:** {details['description']}")
        st.markdown(f"**Objetivo:** {details['objective']}")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("Sprints - Keilon")
            if "Keilon" in details["sprints"]:
                for sprint_data in details["sprints"]["Keilon"]:
                    st.markdown(f"""
                    <div class="sprint-task">
                        <strong>Sprint {sprint_data['sprint']}:</strong> {sprint_data['task']} <br>
                        <em>{sprint_data['hours']} horas</em>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("Nenhuma sprint designada para Keilon.")
        with col2:
            st.subheader("Sprints - Thiago")
            if "Thiago" in details["sprints"]:
                for sprint_data in details["sprints"]["Thiago"]:
                    st.markdown(f"""
                    <div class="sprint-task">
                        <strong>Sprint {sprint_data['sprint']}:</strong> {sprint_data['task']} <br>
                        <em>{sprint_data['hours']} horas</em>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("Nenhuma sprint designada para Thiago.")
        with col3:
            st.subheader("Sprints - Ricardo")
            if "Ricardo" in details["sprints"]:
                for sprint_data in details["sprints"]["Ricardo"]:
                    st.markdown(f"""
                    <div class="sprint-task">
                        <strong>Sprint {sprint_data['sprint']}:</strong> {sprint_data['task']} <br>
                        <em>{sprint_data['hours']} horas</em>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("Nenhuma sprint designada para Ricardo.")
        with col4:
            st.subheader("Sprints - Alberth")
            if "Alberth" in details["sprints"]:
                for sprint_data in details["sprints"]["Alberth"]:
                    st.markdown(f"""
                    <div class="sprint-task">
                        <strong>Sprint {sprint_data['sprint']}:</strong> {sprint_data['task']} <br>
                        <em>{sprint_data['hours']} horas</em>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("Nenhuma sprint designada para Alberth.")
st.write("---")

# =============================================================================
# 7. PRODUTIVIDADE: FERRAMENTAS E ESTRATÉGIAS
# =============================================================================
st.subheader("Produtividade: Ferramentas e Estratégias")
st.write("""
- **Centralização:** Utilização de Jira, Asana ou Notion para gerenciamento de backlogs e sprints.
- **Alertas e Automação:** Make.com para alertas e relatórios em tempo real.
- **Reuniões Ágeis:** Daily Stand-ups (15 min) e reuniões estratégicas (30-60 min, 3x por semana).
- **Base de Conhecimento:** Documentação detalhada e acessível das integrações e processos.
- **Gestão de Escopo:** Definição clara de limites e reconhecimento das restrições técnicas.
""")
st.write("---")

# =============================================================================
# 8. FERRAMENTAS E CUSTOS (PRÉVIA)
# =============================================================================
st.subheader("Ferramentas e Custos")
ferramentas = [
    {"Ferramenta": "ChatGPT", "Descrição": "Assistente de IA e geração de conteúdo", "Custo": "Gratuito / ChatGPT Plus: US$20/mês"},
    {"Ferramenta": "ManyChat", "Descrição": "Plataforma de automação de chatbots", "Custo": "A partir de US$10/mês (varia conforme assinantes)"},
    {"Ferramenta": "Tray", "Descrição": "Plataforma de ecommerce", "Custo": "Planos a partir de R$49/mês"},
    {"Ferramenta": "Olist CMS Ecommerce", "Descrição": "Solução CMS para ecommerce", "Custo": "A partir de R$200/mês (aproximado)"},
    {"Ferramenta": "Bling", "Descrição": "ERP e gestão para ecommerce", "Custo": "Planos a partir de R$29/mês"}
]
ferramentas_df = pd.DataFrame(ferramentas)
st.table(ferramentas_df)
st.write("---")

# =============================================================================
# 9. FLUXO DE TRABALHO SCRUM
# =============================================================================
st.subheader("Fluxo de Trabalho Scrum: Iterativo e Adaptável")
st.write("""
Adotamos o framework **Scrum** para estruturar nossos ciclos de entrega em sprints de 2 semanas, garantindo feedback rápido e adaptação contínua. O fluxograma abaixo ilustra o processo:
""")
if graphviz_installed:
    flowchart = """
    digraph G {
        rankdir=TB;
        node [shape=box, style="rounded,filled", fillcolor="#DAE8FC", color="#6C8EBF", fontcolor="#333333", fontsize=12, margin="0.2,0.1"];
        edge [color="#6C8EBF", fontcolor="#333333"];

        Stakeholder [label="Stakeholder", fillcolor="#B9D0EE"];
        Client [label="Client Liaison", fillcolor="#B9D0EE"];
        ProductOwner [label="Product Owner\n(Ricardo)"];
        ProductBacklog [label="Product Backlog"];
        SprintBacklog [label="Sprint Backlog"];
        SprintStart [label="Sprint Start"];
        DailyScrum [label="Daily Scrum\n(15 min)"];
        SprintReview [label="Sprint Review"];
        SprintRetrospective [label="Sprint Retrospective"];
        BacklogRefinement [label="Backlog Refinement"];
        FinalDelivery [label="Entrega Final", shape=doublecircle, fillcolor="#90EE90"];

        Stakeholder -> Client;
        Client -> ProductOwner;
        ProductOwner -> ProductBacklog;
        ProductBacklog -> SprintBacklog [label="Selecionar Itens"];
        SprintBacklog -> SprintStart;
        SprintStart -> DailyScrum;
        DailyScrum -> SprintReview [label="Fim da Sprint"];
        SprintReview -> SprintRetrospective [label="Feedback"];
        SprintRetrospective -> BacklogRefinement [label="Ajustes"];
        BacklogRefinement -> ProductBacklog [label="Atualização"];
        SprintReview -> FinalDelivery [label="Lançamento"];

        {rank=same; SprintReview; SprintRetrospective}
    }
    """
    st.graphviz_chart(flowchart)
else:
    st.warning("Graphviz não está instalado.")
st.write("---")

# =============================================================================
# 10. CONSIDERAÇÕES FINAIS
# =============================================================================
st.subheader("Considerações Finais")
st.write("""
Esta proposta foi elaborada para transformar digitalmente sua organização, promovendo agilidade, inovação e resultados mensuráveis.  
Com o uso do **Scrum**, integração de automações e foco em dados, estamos preparados para transformar desafios em oportunidades de crescimento e sucesso.
""")
st.success("Obrigado por analisar esta proposta. Vamos transformar seus objetivos em realidade!")
