
from flask import Flask, request, jsonify, make_response, send_from_directory

def sieve_of_erastothenoss(n):
    numbers = [True] * (n + 1)
    
    numbers[0] = False
    numbers[1] = False
    
    primes = []
    
    for number, prime in enumerate(numbers):
        if prime:
            primes.append(number)
            for i in range(number * 2, n + 1, number):
                numbers[i] = False

    return primes

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

@app.route('/sieve/<n>', methods =['GET'])
def sieve(n):

    n = int(n)
    l = sieve_of_erastothenoss(n)
  
    return make_response(l)

# curl -X POST -d '{"n": 199}' -H "Content-Type: application/json" localhost:5000/sieve
