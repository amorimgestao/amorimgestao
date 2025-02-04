import streamlit as st
import pandas as pd

# =============================================================================
# Page Configuration
# =============================================================================
st.set_page_config(page_title="HRV Dashboard", layout="wide", page_icon=":bar_chart:")

# CSS custom styling
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #333;
            font-family: 'Segoe UI', sans-serif;
        }
        .main > div:first-child {
            background-color: #ffffff;
            padding: 1rem 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
            color: #4a90e2;
            font-size: 14px;
            margin-left: 4px;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 250px;
            background-color: #555;
            color: #fff;
            text-align: left;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -125px;
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 9px;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
""", unsafe_allow_html=True)

st.title("HRV Dashboard - December vs. January Comparison")

# =============================================================================
# Metrics Data
# =============================================================================
metrics = [
    # Metric details are unchanged
    {
        "name": "Receita",
        "jan": 15191.00,
        "dec": 15191.00 + 2706.00,
        "delta_val": -2706.00,
        "delta_perc": -13.67,
        "type": "revenue",
        "explanation": ("A Receita representa o total de dinheiro recebido pela empresa a partir das vendas ou serviços prestados. "
                        "Uma queda na receita pode indicar uma diminuição nas vendas ou perda de clientes, o que é negativo.")
    },
    # ... other metrics ...
    {
        "name": "Juros Recebido",
        "jan": 300.00,
        "dec": 300.00 - 204.00,
        "delta_val": +204.00,
        "delta_perc": +312.5,
        "type": "revenue",
        "explanation": ("Juros Recebidos são os encargos cobrados dos clientes inadimplentes, representando dinheiro extra que entra na empresa. "
                        "Um aumento neste valor é positivo, indicando mais recursos, embora possa também sinalizar problemas de inadimplência.")
    }
]

# =============================================================================
# Utility Functions
# =============================================================================
def tooltip_html(text):
    """Generate HTML for tooltip."""
    return f'<span class="tooltip">ℹ️<span class="tooltiptext">{text}</span></span>'

def render_metric(metric):
    """Render a single metric card with its value and delta."""
    title_html = f"<span style='font-weight:bold;'>{metric['name']}</span>{tooltip_html(metric['explanation'])}"
    st.markdown(title_html, unsafe_allow_html=True)
    st.markdown("<div style='margin-top: -10px;'></div>", unsafe_allow_html=True)

    # Format values
    value_str = f"{metric['jan']:.2f}%" if metric["name"] == "% Custo Asaas" else f"R$ {metric['jan']:,.2f}"
    delta_str = f"R$ {abs(metric['delta_val']):,.2f}" if metric["name"] != "% Custo Asaas" else f"{abs(metric['delta_val']):.2f}%"
    
    delta_perc_display = f"{abs(metric['delta_perc']):.2f}%" if metric['delta_perc'] is not None else ""
    delta_display = f"{'-' if metric['delta_val'] < 0 else '+'}{delta_str} ({'-' if metric['delta_perc'] < 0 else '+'}{delta_perc_display})"
    
    # Determine delta color
    delta_color = "normal" if metric["type"] == "revenue" else "inverse"
    
    st.metric(label="", value=value_str, delta=delta_display, delta_color=delta_color)

# =============================================================================
# Display Metrics
# =============================================================================
st.markdown("### Key Indicators")
num_cols = 4
cols = st.columns(num_cols)

for i, metric in enumerate(metrics):
    with cols[i % num_cols]:
        render_metric(metric)

st.markdown("<hr><p style='text-align: center; color: #666;'>HRV Dashboard © 2025</p>", unsafe_allow_html=True)
