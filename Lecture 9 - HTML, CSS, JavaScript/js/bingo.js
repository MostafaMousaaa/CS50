// CS50-themed bingo phrases
const bingoTexts = [
    "This is CS50!",
    "Understanding underneath the hood",
    "Correctness, design, style",
    "Big O notation",
    "Segmentation fault",
    "Memory leak",
    "malloc() and free()",
    "Rubber duck debugging",
    "Off by one error",
    "David says 'Indeed'",
    "Live coding demo",
    "Student question",
    "Zoom chat comment",
    "CS50 Duck mentioned",
    "Algorithm explanation",
    "Pseudocode on screen",
    "Binary representation",
    "Linked list discussion",
    "Hash table collision",
    "Recursion example",
    "Array indexing",
    "Pointer arithmetic",
    "SQL injection warning",
    "Regular expressions",
    "TCP/IP explanation",
    "HTTP status codes",
    "DOM manipulation",
    "Event listener",
    "CSS selector",
    "JavaScript function",
    "Responsive design",
    "Bootstrap grid",
    "AJAX request",
    "JSON format",
    "API endpoint",
    "Database query",
    "Primary key",
    "Foreign key",
    "Machine learning",
    "Neural network",
    "Decision tree",
    "Minimax algorithm",
    "AI ethics",
    "Prompt engineering",
    "Large language model",
    "Computer vision",
    "Image processing",
    "Face recognition",
    "Natural language processing"
];

let currentBoard = [];
let selectedTexts = [];

function generateRandomBoard() {
    // Shuffle and select 24 random texts (25th will be FREE)
    const shuffled = [...bingoTexts].sort(() => 0.5 - Math.random());
    selectedTexts = shuffled.slice(0, 24);
    
    // Insert FREE space in the middle (index 12)
    selectedTexts.splice(12, 0, "FREE SPACE");
    
    return selectedTexts;
}

function createBoard() {
    const board = document.getElementById('bingoBoard');
    board.innerHTML = '';

    // Create headers
    const headers = ['B', 'I', 'N', 'G', 'O'];
    headers.forEach(letter => {
        const header = document.createElement('div');
        header.className = 'bingo-header';
        header.textContent = letter;
        board.appendChild(header);
    });

    // Create board cells
    for (let i = 0; i < 25; i++) {
        const cell = document.createElement('div');
        cell.className = 'bingo-cell';
        cell.textContent = currentBoard[i];
        cell.setAttribute('data-index', i);
        
        if (i === 12) { // Free space
            cell.classList.add('free-space', 'marked');
        } else {
            cell.addEventListener('click', () => toggleCell(i));
        }
        
        board.appendChild(cell);
    }
}

function toggleCell(index) {
    const cell = document.querySelector(`[data-index="${index}"]`);
    cell.classList.toggle('marked');
    
    // Check for win after each click
    setTimeout(checkWin, 100);
}

function checkWin() {
    const cells = document.querySelectorAll('.bingo-cell');
    const marked = Array.from(cells).map(cell => cell.classList.contains('marked'));
    
    // Check rows
    for (let row = 0; row < 5; row++) {
        if (marked.slice(row * 5, row * 5 + 5).every(Boolean)) {
            showWin('Row ' + (row + 1));
            return true;
        }
    }
    
    // Check columns
    for (let col = 0; col < 5; col++) {
        if ([0, 1, 2, 3, 4].every(row => marked[row * 5 + col])) {
            showWin('Column ' + (col + 1));
            return true;
        }
    }
    
    // Check diagonals
    if ([0, 6, 12, 18, 24].every(i => marked[i])) {
        showWin('Diagonal (top-left to bottom-right)');
        return true;
    }
    
    if ([4, 8, 12, 16, 20].every(i => marked[i])) {
        showWin('Diagonal (top-right to bottom-left)');
        return true;
    }
    
    // Update status
    const markedCount = marked.filter(Boolean).length;
    document.getElementById('status').textContent = 
        `${markedCount} squares marked. Keep going!`;
    document.getElementById('status').className = 'status';
    
    return false;
}

function showWin(winType) {
    const status = document.getElementById('status');
    status.textContent = `🎉 BINGO! You won with ${winType}! 🎉`;
    status.className = 'status winner';
    
    // Celebrate with confetti effect
    createConfetti();
}

function createConfetti() {
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.style.position = 'fixed';
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.top = '-10px';
        confetti.style.width = '10px';
        confetti.style.height = '10px';
        confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 70%, 60%)`;
        confetti.style.pointerEvents = 'none';
        confetti.style.zIndex = '1000';
        document.body.appendChild(confetti);
        
        // Animate falling
        confetti.animate([
            { transform: 'translateY(0) rotate(0deg)', opacity: 1 },
            { transform: `translateY(100vh) rotate(${Math.random() * 360}deg)`, opacity: 0 }
        ], {
            duration: Math.random() * 2000 + 1000,
            easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
        }).onfinish = () => confetti.remove();
    }
}

function resetBoard() {
    const cells = document.querySelectorAll('.bingo-cell');
    cells.forEach((cell, index) => {
        if (index !== 12) { // Don't reset free space
            cell.classList.remove('marked');
        }
    });
    
    document.getElementById('status').textContent = 'Board reset! Click squares as events happen!';
    document.getElementById('status').className = 'status';
}

function generateNewBoard() {
    currentBoard = generateRandomBoard();
    createBoard();
    document.getElementById('status').textContent = 'New board generated! Good luck!';
    document.getElementById('status').className = 'status';
}

// Initialize the board when page loads
window.addEventListener('DOMContentLoaded', () => {
    currentBoard = generateRandomBoard();
    createBoard();
});

// Add some fun keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'r' || e.key === 'R') {
        resetBoard();
    } else if (e.key === 'n' || e.key === 'N') {
        generateNewBoard();
    } else if (e.key === 'c' || e.key === 'C') {
        checkWin();
    }
});