import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

# =============================================================================
# 1. CONFIGURAÇÕES INICIAIS DA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Proposta - Planejamento de Entregas",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =============================================================================
# 2. ESTILOS / CSS CUSTOMIZADO
# =============================================================================
custom_css = """
<style>
/* Fonte principal e fundo */
body {
    font-family: 'Arial', sans-serif;
    background-color: #F9FAFC;
}

/* Títulos */
h1, h2, h3 {
    color: #2F5597;
}

/* Container principal */
.block-container {
    border-radius: 10px;
    padding: 1.5rem 2rem;
}

/* Barras de progresso e botões */
.css-18ni7ap, .stProgress > div > div > div > div {
    background: linear-gradient(90deg, #2F5597, #5B9BD5);
}

/* Expanders */
.stExpander {
    background-color: #F0F4F8;
    border-radius: 8px;
    border: 1px solid #c5d0e6;
    padding: 0.5rem;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# =============================================================================
# 3. CABEÇALHO DO DASHBOARD
# =============================================================================
st.title("Proposta de Planejamento de Entregas")
st.caption("Product Owner: **Ricardo Menendez Sarmento**")
st.write("---")

st.subheader("Visão Geral (4 meses, 280 horas)")
st.write("""
Elaborei um planejamento para entregar **MVPs funcionais** de todos os projetos, 
considerando **70 horas mensais** (cerca de 15–20 horas semanais). Ressalto que, 
devido à limitação de horas, o sucesso dependerá de um escopo bem definido e da 
colaboração constante com as equipes de desenvolvimento, dados e marketing.
""")
st.write("""
**Minhas responsabilidades**:
- Alinhar prioridades e detalhar requisitos com os clientes.
- Documentar e organizar as demandas (Jira, Asana ou Notion).
- Acompanhar entregas e manter o backlog priorizado.
- Validar MVPs e automações, fornecendo feedback à equipe técnica.
""")

# =============================================================================
# 4. CRONOGRAMA SIMPLIFICADO (BARRAS DE PROGRESSO)
# =============================================================================
st.write("---")
st.subheader("Cronograma Simplificado")
cols = st.columns(4)

with cols[0]:
    st.write("**Mês 1**")
    st.write("• Levantamento Detalhado\n• Mapeamento de Funis\n• Organização e Integrações Básicas")
    st.progress(0.25)

with cols[1]:
    st.write("**Mês 2**")
    st.write("• Desenvolvimento e Validação dos MVPs\n• Teste do Chatbot/IA\n• Ajustes no Monitoramento")
    st.progress(0.0)

with cols[2]:
    st.write("**Mês 3**")
    st.write("• Refinamento de Interfaces\n• Otimização de Conversão\n• Aprimoramento dos Fluxos")
    st.progress(0.0)

with cols[3]:
    st.write("**Mês 4**")
    st.write("• Go-Live e Revisões Finais\n• Documentação Completa\n• Entrega do 'Estado Final'")
    st.progress(0.0)

st.info("**Observação:** Percentuais ilustrativos; o cronograma será atualizado conforme o progresso real.")

# =============================================================================
# 5. DETALHES DOS PROJETOS
# =============================================================================
st.write("---")
st.subheader("Fatores-Chave para Cada Projeto")

projetos = {
    "1. Fênix Telecom": [
        "Funil de vendas direto no site (checkout integrado)",
        "Automação de pedidos",
        "Integração com Olist (opcional, se houver tempo)"
    ],
    "2. Chalé": [
        "Funil de vendas em site PWA (mobile-friendly)",
        "Experiência de usuário focada em reservas"
    ],
    "3. AGX Capital": [
        "Site institucional + IA de atendimento",
        "Automação avançada (foco em comportamento do usuário)"
    ],
    "4. Brprix Transportes": [
        "Monitoramento de motoristas (GPS, alertas)",
        "Funil de vendas automatizado (site e WhatsApp)",
        "Projeto de maior complexidade técnica (risco mais elevado)"
    ],
    "5. DHE Componentes Hidráulicos": [
        "Site para venda de serviços",
        "Funil de vendas automatizado (captura de leads, chatbot)"
    ],
}

for nome_projeto, detalhes in projetos.items():
    with st.expander(nome_projeto, expanded=False):
        for bullet in detalhes:
            st.write(f"- {bullet}")

# =============================================================================
# 6. DICAS DE ORGANIZAÇÃO E PRODUTIVIDADE
# =============================================================================
st.write("---")
st.subheader("Dicas de Organização e Produtividade")
st.write("""
1. **Centralização:** Utilizo Jira, Asana ou Notion para todos os backlogs, boards de tarefas e acompanhamento de sprints.  
2. **Automação:** Configuro alertas e relatórios automáticos via Make.com para cada fase concluída.  
3. **Reuniões:** Realizo encontros rápidos (30 a 60 min 3 vezes semanais) para alinhar prioridades, além de uma reunião mensal mais extensa para revisão de status.  
4. **Documentação:** Registro cada automação e integração de forma detalhada para facilitar suporte e evolução dos projetos.  
5. **Gerenciamento de Escopo:** Reforço as limitações de horas e restrições técnicas para evitar alterações de última hora que possam comprometer prazos e qualidade.
""")

# =============================================================================
# 7. FLUXOGRAMA DO FLUXO DE TRABALHO (SCRUM) USANDO GRAPHVIZ
# =============================================================================
st.write("---")
st.subheader("Fluxograma do Fluxo de Trabalho (Scrum)")

flowchart = r"""
digraph G {
    rankdir=TB;
    node [shape=box, style="rounded,filled", fillcolor="#F0F4F8", color="#2F5597", fontcolor="#2F5597", fontsize=12, margin="0.2,0.1"];
    
    Stakeholder [label="Stakeholder\n(Parte Interessada)"];
    Liaison [label="Cliente"];
    ProjectOwner [label="Project Owner\n(Gerente do Produto)"];
    ProductBacklog [label="Product Backlog\n(Lista de Funcionalidades)"];
    SprintBacklog [label="Sprint Backlog\n(Tarefas para a Sprint)"];
    Inicio [label="Início da Sprint"];
    RoutineScrum [label="Routine Scrum\n(15 min diários)"];
    SprintAssessment [label="Sprint Assessment\n(Review)"];
    SprintRetrospective [label="Sprint Retrospective\n(Retrospectiva)"];
    Refinamento [label="Refinamento do Backlog"];
    FinalEntrega [label="Entrega Final"];

    Stakeholder -> Liaison;
    Liaison -> ProjectOwner;
    ProjectOwner -> ProductBacklog;
    ProductBacklog -> SprintBacklog [label="Selecionar Itens"];
    SprintBacklog -> Inicio [label="Início da Sprint"];
    Inicio -> RoutineScrum;
    RoutineScrum -> SprintAssessment [label="Final da Sprint"];
    SprintAssessment -> SprintRetrospective [label="Feedback"];
    SprintRetrospective -> Refinamento [label="Ajustes"];
    Refinamento -> ProductBacklog [label="Atualização"];
    SprintAssessment -> FinalEntrega [label="Entrega Final"];
}
"""
st.graphviz_chart(flowchart)

# =============================================================================
# 8. CONSIDERAÇÕES FINAIS
# =============================================================================
st.write("---")
st.subheader("Considerações Finais")
st.write("""
Com um planejamento enxuto e um escopo bem definido, estou confiante em entregar **MVPs funcionais** 
em 4 meses, mesmo com a pressão de um cronograma apertado. Minha função como Product Owner é priorizar, planejar 
e acompanhar cada etapa, contando com o suporte integral da equipe técnica e do Head de Dados, Tecnologia e Marketing.
""")
st.success("Fim da apresentação! Obrigado por conferir este dashboard de proposta.")
