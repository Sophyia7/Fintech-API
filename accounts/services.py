from transactions.models import Wallet

def create_user_wallet(user):
	wallet = Wallet.objects.create(user=user)
	wallet.save()
	return wallet

