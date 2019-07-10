import sys
import hashlib
import requests

from blockchain import blockchain, node_identifier


# TODO: Implement functionality to search for a proof


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        URL = "http://localhost:5000/last_proof"
        r = requests.get(URL)
        last_proof = r.json()["last_proof"]

        new_proof = blockchain.proof_of_work(last_proof)

        print(last_proof)
        print(new_proof)

        # TODO: When found, POST it to the server {"proof": new_proof}

        proof_json = {
            "proof": new_proof,
            "client_node_identifier": node_identifier
        }

        payload = proof_json
        MINE_URL = 'http://localhost:5000/mine'
        mine_r = requests.post(MINE_URL, payload)
        print(mine_r.json())

        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
