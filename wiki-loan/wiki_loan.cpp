#include<iostream>
#include<cstring>

using namespace std;

int main()
{
	char name[25],RegID,Bank_acc,loanserv;
	int annsal,reqloan,nin;
	
	cout<<"Welcome to Wiki loan\n";
	cout<<"Input your name:\n";
	cin.getline(name,25);
	cout<<"Input your NIN number\n";
	cin>>nin;
	
	cout<<"Do you have a Registration ID?\n";
	cin>>RegID;
	if(RegID=='Y')
	{
		cout<<"Do you have Bank Account\n";
		cin>>Bank_acc;
		if(Bank_acc=='Y')
		{
			cout<<"Enter your Annual salary\n";
			cin>>annsal;
			cout<<"Enter your Requested loan\n";
			cin>>reqloan;
			if(reqloan<(annsal/3))
			{
				cout<<"Are you servicing a loan right now?\n";
				cin>>loanserv;
				if(loanserv=='N')
				{
					cout<<"You can witdraw a loan";
				}else cout<<"YOU CAN'T\n";
			}else cout<<"you are not eligible";
		}else cout<<"get a bank acc";
		
	}else cout<<"get a reg id";
	
}
