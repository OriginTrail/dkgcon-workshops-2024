import json
from dotenv import load_dotenv
import os

from dkg import DKG
from dkg.providers import BlockchainProvider, NodeHTTPProvider

load_dotenv()


def divider():
    print("==================================================")
    print("==================================================")
    print("==================================================")


def print_json(json_dict: dict):
    print(json.dumps(json_dict, indent=4))


node_provider = NodeHTTPProvider("https://v8-testnet-09.origin-trail.network:8900")
blockchain_provider = BlockchainProvider(
    "testnet",
    "base:84532",
    private_key=os.getenv("PRIVATE_KEY"),
)

dkg = DKG(node_provider, blockchain_provider)

content = {
    "public": {
        "@context": "https://schema.org",
        "@type": "Event",
        "name": "DKGCon 2024",
        "description": "The Decentralized Knowledge Conference (DKGCon).",
        "location": {
            "@type": "Place",
            "name": "Sam's Koffie",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Meeuwenlaan 126B",
                "addressLocality": "Amsterdam",
                "addressRegion": "NH",
                "postalCode": "1021 JN",
                "addressCountry": "NL"
            }
        },
        "subEvent": {
            "@type": "Event",
            "name": "Workshop #1",
            "description": "A workshop focused on the basics of the DKG.",
            "performer": [
            {
                "@type": "Person",
                "name": "Branimir Rakic",
                "jobTitle": "CTO"
            },
            {
                "@type": "Person",
                "name": "Uladzislau Hubar",
                "jobTitle": "Protocols Engineer"
            }
            ]
        },
        "keywords": [
            "Decentralized Knowledge",
            "Blockchain",
            "Web3",
            "OriginTrail",
            "Digital Trust"
        ],
    },
}

info_result = dkg.node.info

print("======================== NODE INFO RECEIVED")
print_json(info_result)
divider()

# epochs are measured as 1 epochs = 3 months for incentivised storage
# of knowledge assets

# optionally provide token amount to lock to store on more nodes
epochs = 2
token_amount = 0
create_asset_result = dkg.asset.create(content, epochs, token_amount)
print("======================== ASSET CREATED")
print_json(create_asset_result)
divider()

get_asset_result = dkg.asset.get(create_asset_result["UAL"])
print("======================== ASSET RESOLVED")
print_json(get_asset_result)
divider()
