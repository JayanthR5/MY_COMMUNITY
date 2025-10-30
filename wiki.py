import wikipediaapi
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='SustainabilityAgent/1.0 (contact: your_email@example.com)'
)

topics = [
    "Recycling", "Waste management", "Composting", "Biodegradable waste",
    "Plastic recycling", "Electronic waste", "Sustainability", "Circular economy",
    "Hazardous waste", "Recyclable materials", "Environmental impact of plastics",
    "Zero waste", "Organic waste", "Recycling by material", "Plastic pollution",
    "E-waste recycling", "Compostable plastic", "Upcycling", "Waste segregation", "Landfill"
]

data = []

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

for topic in topics:
    page = wiki.page(topic)
    if not page.exists():
        print(f"⚠️ Skipping missing page: {topic}")
        continue

    print(f"✅ Adding: {topic}")

    chunks = splitter.split_text(page.text)
    for chunk in chunks:
        data.append({"Title": topic, "Content": chunk})

df = pd.DataFrame(data)
df.to_csv("sustainability_knowledge.csv", index=False)
print("✅ Dataset saved to sustainability_knowledge.csv")