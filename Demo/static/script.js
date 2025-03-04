document.addEventListener('DOMContentLoaded', () => {
    const balanceElement = document.getElementById('balance');
    const amountInput = document.getElementById('amount');
    const depositBtn = document.getElementById('depositBtn');
    const withdrawBtn = document.getElementById('withdrawBtn');
    const transactionHistory = document.getElementById('transactionHistory');

    // Initial balance fetch
    fetchBalance();

    // Event listeners for buttons
    depositBtn.addEventListener('click', () => handleTransaction('deposit'));
    withdrawBtn.addEventListener('click', () => handleTransaction('withdraw'));

    // Add hover effect to buttons
    [depositBtn, withdrawBtn].forEach(btn => {
        btn.addEventListener('mouseover', () => {
            btn.style.transform = 'translateY(-2px)';
            btn.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
        });

        btn.addEventListener('mouseout', () => {
            btn.style.transform = 'translateY(0)';
            btn.style.boxShadow = 'none';
        });
    });

    // Handle input validation
    amountInput.addEventListener('input', (e) => {
        const value = e.target.value;
        if (value < 0) {
            e.target.value = 0;
        }
    });

    async function fetchBalance() {
        try {
            const response = await fetch('/balance');
            const data = await response.json();
            updateBalance(data.balance);
        } catch (error) {
            console.error('Error fetching balance:', error);
        }
    }

    async function handleTransaction(type) {
        const amount = parseFloat(amountInput.value);
        if (!amount || amount <= 0) {
            showNotification('Please enter a valid amount', 'error');
            return;
        }

        try {
            const response = await fetch(`/${type}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ amount }),
            });

            const data = await response.json();
            
            if (response.ok) {
                updateBalance(data.balance);
                updateTransactionHistory(data.transactions);
                showNotification(data.message, 'success');
                amountInput.value = '';
            } else {
                showNotification(data.error || 'Transaction failed', 'error');
            }
        } catch (error) {
            console.error(`Error processing ${type}:`, error);
            showNotification('Transaction failed', 'error');
        }
    }

    function updateBalance(balance) {
        balanceElement.textContent = `$${balance.toFixed(2)}`;
        balanceElement.classList.add('balance-update');
        setTimeout(() => {
            balanceElement.classList.remove('balance-update');
        }, 500);
    }

    function updateTransactionHistory(transactions) {
        transactionHistory.innerHTML = '';
        transactions.forEach(transaction => {
            const isDeposit = transaction.includes('Deposit');
            const div = document.createElement('div');
            div.className = `transaction-item ${isDeposit ? 'deposit' : 'withdrawal'}`;
            div.textContent = transaction;
            transactionHistory.insertBefore(div, transactionHistory.firstChild);
        });
    }

    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        document.body.appendChild(notification);

        // Add styles dynamically
        notification.style.position = 'fixed';
        notification.style.top = '20px';
        notification.style.right = '20px';
        notification.style.padding = '1rem 2rem';
        notification.style.borderRadius = '5px';
        notification.style.color = 'white';
        notification.style.backgroundColor = type === 'success' ? '#1e90ff' : '#ff6b6b';
        notification.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
        notification.style.zIndex = '1000';
        notification.style.animation = 'slideIn 0.3s ease-out';

        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }

    // Add animation keyframes
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideOut {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
}); 