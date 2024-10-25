# dkgcon-workshops-2024

[Workshop Slides](https://docs.google.com/document/d/1MtFpaZypd1eg5AcSir1B9VAZSLTUelITGUX3U27wyPk/edit)

## Setup

* Clone repo
```bash
git clone https://github.com/OriginTrail/dkgcon-workshops-2024
cd dkgcon-workshops-2024
```
* Generate .env file
```
cp .env_example .env
```
* Create EVM wallet and save it privately and securely.
* Add Base Sepolia network to Metamask or similar https://docs.base.org/docs/using-base/#testnet
* Request Base Sepolia Testnet tokens from the faucet for the public address of your wallet https://docs.base.org/docs/tools/network-faucets/
* Add private key to .env file
* Run Docker container in detached mode
```bash
docker-compose up --build workshop -d
docker ps -a
```
* Enter Docker container
```
docker exec --workdir /workshop -it workshop-workshop-1 /bin/bash
```

* Optional: View Docker container logs
```
docker-compose logs --tail=1000 -f workshop
```

## Exercise 1: Create Knowledge Asset

* Run Python script inside the Docker container
```bash
python3 create_knowledge_asset.py
```

* View transaction on Base Sepolia block explorer https://sepolia-explorer.base.org

## Exercise 2: Transfer Asset

Try to 
```
new_owner = "0x"
ual = "did"
assert_transfer_result - dkg.asset.transfer(ual, new_owner)
```

## Resources:

[DKG.py Client](https://docs.origintrail.io/dkg-v8-upcoming-version/v8-dkg-sdk/dkg-v8-py-client)
