class BankAccount{

    constructor(name, balance){
        this.name = name;
        this.balance = balance;
    }

    deposit(amount){
        this.balance += amount;
    }

    withdraw(amount){
        if ((this.balance - amount) > 0){
            this.balance -= amount
        }else{
            console.log("Error: insufficient funds!");
        }
    }

    logEvent(time, tran, amount, old, newB){
        this.time = time;
        this.tran = tran;
        this.amount = amount;
        this.old = old;
        this.newB = newB;
    }

    logArr(){
        
    }
}