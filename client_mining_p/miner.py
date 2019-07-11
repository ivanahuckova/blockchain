import sys
import hashlib
import requests
from flask import jsonify
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

        print('PROOF OF WORK STATUS: MINING IN PROGRESS')
        new_proof = blockchain.proof_of_work(last_proof)
        print('PROOF OF WORK STATUS: MINING COMPLETE')
        # print(last_proof)
        # print(new_proof)

        # TODO: When found, POST it to the server {"proof": new_proof}

        proof_json = {
            "proof": new_proof
            # "client_node_identifier": node_identifier
        }

        payload = proof_json
        MINE_URL = 'http://localhost:5000/mine'
        mine_r = requests.post(MINE_URL, json=payload)
        # print(mine_r)

        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        mine_r_json = mine_r.json()
        if mine_r_json['message'] == 'New Block Forged':
            coins_mined += 1
            print(f"Coins mined: {coins_mined}")
        # Otherwise, print the failure message from the server
        else:
            print(mine_r_json['failure'])
