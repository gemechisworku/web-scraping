import streamlit as st
import pandas as pd
import io
from scraper import scrape_conselho_geral, scrape_fields_page

# Config
st.set_page_config(page_title="OA Scraper", layout="wide")

SOURCES = {
    "Conselho Geral Contacts": {
        "url": "https://portal.oa.pt/contactos/conselho-geral/",
        "type": "contacts"
    },
    "Lawyer Search Page": {
        "url": "https://portal.oa.pt/advogados/pesquisa-de-advogados/",
        "type": "fields"
    },
    "Law Firm Search Page": {
        "url": "https://portal.oa.pt/advogados/pesquisa-de-sociedades-de-advogados/",
        "type": "fields"
    }
}

if 'results' not in st.session_state:
    st.session_state.results = {}

st.title("📊 OA Web Scraper Dashboard")
tabs = st.tabs(list(SOURCES.keys()))

for i, (name, config) in enumerate(SOURCES.items()):
    with tabs[i]:
        url = config["url"]
        st.markdown(f"#### 🔗 [{url}]({url})")
        if st.button(f"Scrape {name}", key=f"btn_{i}"):
            with st.spinner(f"Scraping {name}..."):
                if config["type"] == "contacts":
                    df = scrape_conselho_geral(url)
                else:
                    df = scrape_fields_page(url)
                st.session_state.results[name] = df
                st.success(f"✅ {name} scraped successfully!")

        if name in st.session_state.results:
            df = st.session_state.results[name]
            st.markdown("#### 📋 Results")
            if df.shape[1] == 1:
                st.write(df.to_markdown(index=False), unsafe_allow_html=True)
            else:
                st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label=f"⬇️ Download {name} CSV",
                data=csv,
                file_name=f"{name.replace(' ', '_').lower()}.csv",
                mime="text/csv",
                key=f"{name}_csv"
            )

# Download All (Excel)
if len(st.session_state.results) == len(SOURCES):
    st.markdown("---")
    st.subheader("📥 Export All as Excel (Separate Sheets)")

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for name, df in st.session_state.results.items():
            sheet_name = name[:31].replace(" ", "_")
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    output.seek(0)

    st.download_button(
        label="⬇️ Download All in Excel",
        data=output,
        file_name="all_scraped_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="excel_download"
    )

# Footer
st.markdown("""
    <hr style="margin-top: 3rem; margin-bottom: 1rem;">
    <div style='text-align: center; font-size: 0.9rem; color: gray;'>
        Developed by <strong>Gemechis W.</strong> | © 2025
    </div>
""", unsafe_allow_html=True)
