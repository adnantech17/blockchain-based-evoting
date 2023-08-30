from votingSystem import VotingSystem
# Example usage
if __name__ == "__main__":
    keyManager = VotingSystem()
    keyManager.genKeys(256)
    keyManager.savePrivateKey(2, 3)
    keyManager.savePublicKey()
    
    print("Public and private keys generated successfully.")
