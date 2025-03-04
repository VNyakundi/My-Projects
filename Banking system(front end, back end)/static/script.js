document.addEventListener('DOMContentLoaded', () => {
    const balanceElement = document.getElementById('balance');
    const amountInput = document.getElementById('amount');
    const pinInput = document.getElementById('pin');
    const depositBtn = document.getElementById('depositBtn');
    const withdrawBtn = document.getElementById('withdrawBtn');
    const transactionHistory = document.getElementById('transactionHistory');
    const pinSection = document.getElementById('pinSection');
    const transactionSection = document.getElementById('transactionSection');
    const receiptModal = document.getElementById('receiptModal');
    const receiptContent = document.getElementById('receiptContent');
    const closeModal = document.querySelector('.close');
    const printReceiptBtn = document.getElementById('printReceiptBtn');

    let currentPin = '';
    let lastTransactionIndex = -1;

    // Show initial balance
    updateBalance(1000.00);

    // Hide transaction section until PIN is verified
    transactionSection.style.display = 'none';

    // Event listeners for buttons
    depositBtn.addEventListener('click', () => handleTransaction('deposit'));
    withdrawBtn.addEventListener('click', () => handleTransaction('withdraw'));
    closeModal.addEventListener('click', () => receiptModal.style.display = 'none');
    printReceiptBtn.addEventListener('click', () => window.print());

    // PIN input validation and auto-verify
    pinInput.addEventListener('input', async (e) => {
        const value = e.target.value.replace(/[^0-9]/g, '');
        e.target.value = value;
        if (value.length === 4) {
            await verifyPin(value);
        }
    });

    // Amount input validation
    amountInput.addEventListener('input', (e) => {
        const value = e.target.value;
        if (value < 0) {
            e.target.value = 0;
        }
    });

    async function verifyPin(pin) {
        try {
            console.log('Attempting to verify PIN:', pin);
            const response = await fetch('/verify-pin', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ pin: pin }), // Send PIN as string
            });
            
            console.log('Response status:', response.status);
            const data = await response.json();
            console.log('Server response data:', data);
            
            if (data.valid) {
                console.log('PIN verification successful');
                currentPin = pin;
                pinSection.style.display = 'none';
                transactionSection.style.display = 'block';
                showNotification('PIN verified successfully', 'success');
                fetchBalance();
                fetchTransactions();
            } else {
                console.log('PIN verification failed:', data.message);
                showNotification(data.message || 'Invalid PIN', 'error');
                pinInput.value = '';
            }
        } catch (error) {
            console.error('Error during PIN verification:', error);
            showNotification('Error verifying PIN. Please try again.', 'error');
            pinInput.value = '';
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
                body: JSON.stringify({ amount, pin: currentPin }),
            });

            const data = await response.json();
            
            if (response.ok) {
                updateBalance(data.balance);
                updateTransactionHistory(data.transactions);
                showNotification(data.message, 'success');
                amountInput.value = '';
                lastTransactionIndex = data.transactions.length - 1;
                // Automatically show receipt after transaction
                showReceipt(lastTransactionIndex);
            } else {
                showNotification(data.error || 'Transaction failed', 'error');
            }
        } catch (error) {
            console.error(`Error processing ${type}:`, error);
            showNotification('Transaction failed', 'error');
        }
    }

    async function fetchBalance() {
        try {
            const response = await fetch(`/balance?pin=${currentPin}`);
            const data = await response.json();
            if (data.error) {
                showNotification(data.error, 'error');
                return;
            }
            updateBalance(data.balance);
        } catch (error) {
            console.error('Error fetching balance:', error);
        }
    }

    async function fetchTransactions() {
        try {
            const response = await fetch(`/transactions?pin=${currentPin}`);
            const data = await response.json();
            if (data.error) {
                showNotification(data.error, 'error');
                return;
            }
            updateTransactionHistory(data.transactions);
        } catch (error) {
            console.error('Error fetching transactions:', error);
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
        transactions.forEach((transaction, index) => {
            const div = document.createElement('div');
            div.className = `transaction-item ${transaction.type.toLowerCase()}`;
            div.innerHTML = `
                <span>${transaction.type}: $${transaction.amount.toFixed(2)}</span>
                <span>${transaction.timestamp}</span>
            `;
            div.addEventListener('click', () => showReceipt(index));
            transactionHistory.insertBefore(div, transactionHistory.firstChild);
        });
    }

    async function showReceipt(index) {
        try {
            const response = await fetch('/receipt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ transaction_index: index }),
            });

            const data = await response.json();
            
            if (response.ok) {
                receiptContent.textContent = data.receipt;
                receiptModal.style.display = 'block';
                // Add auto-close after 5 seconds
                setTimeout(() => {
                    receiptModal.style.display = 'none';
                }, 5000);
            } else {
                showNotification(data.error || 'Error fetching receipt', 'error');
            }
        } catch (error) {
            console.error('Error fetching receipt:', error);
            showNotification('Error fetching receipt', 'error');
        }
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