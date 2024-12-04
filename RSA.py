from sympy import mod_inverse, gcd, isprime

def factorize_n(n):
    """Factors n into two prime numbers (for demonstration purposes only).
       This is a simplified factorization for educational use;  real-world RSA uses much larger primes and more sophisticated factorization algorithms.
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and isprime(i) and isprime(n // i):
            return i, n // i
    raise ValueError("n is not a product of two primes (or the primes are too large for this simplified factorization)")

def calculate_q(p, q):
    return (p - 1) * (q - 1)

def find_e(d, q):
    #Check if d and q are coprime before calculating modular inverse
    if gcd(d,q) != 1:
        raise ValueError("d and q are not coprime. Choose a different d.")
    return mod_inverse(d, q)

def encrypt_message(m, d, n):
    if m >= n:
        raise ValueError("Message m must be smaller than n.")
    return pow(m, d, n)

def decrypt_message(c, e, n):
    return pow(c, e, n)

def main():
    #Larger, but still easily factorable for demonstration
    N = 667
    d = 7  # Choose a d that is coprime with Q

    try:
        #Factorization is done here.  Important to catch exceptions
        p, q = factorize_n(N)
        print(f"Прості множники: p = {p}, q = {q}")

        Q = calculate_q(p, q)
        print(f"Q = {Q}")

        e = find_e(d, Q)
        print(f"Секретний ключ e = {e}")

        M = 10 #Example message
        if M >= N:
            raise ValueError("Message must be smaller than N")
        C = encrypt_message(M, d, N)
        print(f"Зашифроване повідомлення C = {C}")

        decrypted_M = decrypt_message(C, e, N)
        print(f"Розшифроване повідомлення M = {decrypted_M}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()