// Sample data for autocomplete and search
const searchData = [
    {
        id: 1,
        title: "David J. Malan",
        description: "Professor of Computer Science at Harvard University, teaches CS50",
        category: "people",
        keywords: ["professor", "teacher", "cs50", "harvard", "computer science"]
    },
    {
        id: 2,
        title: "Binary Search",
        description: "Efficient searching algorithm with O(log n) time complexity",
        category: "concepts",
        keywords: ["algorithm", "search", "efficiency", "logarithmic", "sorted"]
    },
    {
        id: 3,
        title: "Harvard University",
        description: "Prestigious university in Cambridge, Massachusetts",
        category: "places",
        keywords: ["university", "cambridge", "education", "ivy league"]
    },
    {
        id: 4,
        title: "CS50: Introduction to Computer Science",
        description: "Harvard's popular computer science course for beginners",
        category: "courses",
        keywords: ["programming", "computer science", "beginner", "online course"]
    },
    {
        id: 5,
        title: "Machine Learning",
        description: "AI technique that enables computers to learn from data",
        category: "concepts",
        keywords: ["ai", "artificial intelligence", "data", "algorithms", "neural networks"]
    },
    {
        id: 6,
        title: "Silicon Valley",
        description: "Technology hub in California, home to major tech companies",
        category: "places",
        keywords: ["technology", "startups", "innovation", "california", "tech companies"]
    },
    {
        id: 7,
        title: "Python Programming",
        description: "High-level programming language popular for beginners",
        category: "concepts",
        keywords: ["programming", "language", "syntax", "beginner friendly", "scripting"]
    },
    {
        id: 8,
        title: "MIT OpenCourseWare",
        description: "Free online course materials from MIT",
        category: "courses",
        keywords: ["free", "education", "mit", "online", "open source"]
    },
    {
        id: 9,
        title: "Linus Torvalds",
        description: "Creator of Linux operating system and Git version control",
        category: "people",
        keywords: ["linux", "git", "open source", "programmer", "finland"]
    },
    {
        id: 10,
        title: "Algorithm Analysis",
        description: "Study of computational complexity and efficiency",
        category: "concepts",
        keywords: ["big o", "complexity", "performance", "efficiency", "time"]
    },
    {
        id: 11,
        title: "Stanford University",
        description: "Leading research university in Silicon Valley",
        category: "places",
        keywords: ["university", "research", "california", "technology", "innovation"]
    },
    {
        id: 12,
        title: "Data Structures",
        description: "Ways of organizing and storing data efficiently",
        category: "concepts",
        keywords: ["arrays", "linked lists", "trees", "graphs", "hash tables"]
    }
];

// State management
let currentFilter = 'all';
let currentHighlight = -1;
let searchTimeout;
let isSearching = false;

// DOM elements
const searchInput = document.getElementById('searchInput');
const suggestionsDiv = document.getElementById('suggestions');
const resultsDiv = document.getElementById('results');
const statsDiv = document.getElementById('stats');
const filterButtons = document.querySelectorAll('.filter-button');

// Autocomplete functionality
function showSuggestions(query) {
    if (!query.trim()) {
        hideSuggestions();
        return;
    }

    const filtered = filterData(query, currentFilter);
    const suggestions = filtered.slice(0, 5); // Show max 5 suggestions

    if (suggestions.length === 0) {
        hideSuggestions();
        return;
    }

    suggestionsDiv.innerHTML = suggestions
        .map((item, index) => `
            <div class="suggestion-item" data-index="${index}" data-id="${item.id}">
                <div class="title">${highlightText(item.title, query)}</div>
                <div class="description">${highlightText(item.description, query)}</div>
                <span class="category">${item.category}</span>
            </div>
        `).join('');

    suggestionsDiv.style.display = 'block';
    currentHighlight = -1;

    // Add click event listeners to suggestions
    suggestionsDiv.querySelectorAll('.suggestion-item').forEach((item, index) => {
        item.addEventListener('click', () => {
            selectSuggestion(index);
        });
    });
}

function hideSuggestions() {
    suggestionsDiv.style.display = 'none';
    currentHighlight = -1;
}

function selectSuggestion(index) {
    const suggestions = suggestionsDiv.querySelectorAll('.suggestion-item');
    if (suggestions[index]) {
        const title = suggestions[index].querySelector('.title').textContent;
        searchInput.value = title;
        hideSuggestions();
        performSearch(title);
    }
}

function highlightText(text, query) {
    if (!query) return text;
    const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
    return text.replace(regex, '<strong>$1</strong>');
}

function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Search functionality
function performSearch(query) {
    if (!query.trim()) {
        displayResults([]);
        updateStats(0, 0);
        return;
    }

    isSearching = true;
    displayLoading();

    // Simulate network delay
    setTimeout(() => {
        const results = filterData(query, currentFilter);
        displayResults(results, query);
        updateStats(results.length, searchData.length);
        isSearching = false;
    }, 300);
}

function filterData(query, category) {
    return searchData.filter(item => {
        // Category filter
        if (category !== 'all' && item.category !== category) {
            return false;
        }

        // Text search
        const searchText = query.toLowerCase();
        return (
            item.title.toLowerCase().includes(searchText) ||
            item.description.toLowerCase().includes(searchText) ||
            item.keywords.some(keyword => keyword.toLowerCase().includes(searchText))
        );
    }).sort((a, b) => {
        // Sort by relevance (title matches first)
        const queryLower = query.toLowerCase();
        const aTitle = a.title.toLowerCase().includes(queryLower);
        const bTitle = b.title.toLowerCase().includes(queryLower);
        
        if (aTitle && !bTitle) return -1;
        if (!aTitle && bTitle) return 1;
        return 0;
    });
}

function displayResults(results, query = '') {
    if (results.length === 0) {
        resultsDiv.innerHTML = `
            <div class="no-results">
                <h3>No results found</h3>
                <p>Try adjusting your search terms or filters.</p>
            </div>
        `;
        return;
    }

    resultsDiv.innerHTML = results
        .map(item => `
            <div class="result-item">
                <h3>${query ? highlightText(item.title, query) : item.title}</h3>
                <p>${query ? highlightText(item.description, query) : item.description}</p>
                <div class="result-meta">
                    Category: ${item.category.charAt(0).toUpperCase() + item.category.slice(1)} • 
                    Keywords: ${item.keywords.join(', ')}
                </div>
            </div>
        `).join('');
}

function displayLoading() {
    resultsDiv.innerHTML = `
        <div class="loading">
            <p>🔍 Searching...</p>
        </div>
    `;
}

function updateStats(resultCount, totalCount) {
    if (resultCount === 0 && !searchInput.value.trim()) {
        statsDiv.textContent = 'Ready to search...';
    } else {
        statsDiv.textContent = `Found ${resultCount} results out of ${totalCount} total items`;
    }
}

// Event listeners
searchInput.addEventListener('input', (e) => {
    const query = e.target.value;

    // Clear previous timeout
    clearTimeout(searchTimeout);

    // Show suggestions immediately
    showSuggestions(query);

    // Debounce search
    searchTimeout = setTimeout(() => {
        performSearch(query);
    }, 500);
});

searchInput.addEventListener('keydown', (e) => {
    const suggestions = suggestionsDiv.querySelectorAll('.suggestion-item');
    
    switch (e.key) {
        case 'ArrowDown':
            e.preventDefault();
            currentHighlight = Math.min(currentHighlight + 1, suggestions.length - 1);
            updateHighlight(suggestions);
            break;
            
        case 'ArrowUp':
            e.preventDefault();
            currentHighlight = Math.max(currentHighlight - 1, -1);
            updateHighlight(suggestions);
            break;
            
        case 'Enter':
            e.preventDefault();
            if (currentHighlight >= 0 && suggestions[currentHighlight]) {
                selectSuggestion(currentHighlight);
            } else {
                hideSuggestions();
                performSearch(e.target.value);
            }
            break;
            
        case 'Escape':
            hideSuggestions();
            break;
    }
});

function updateHighlight(suggestions) {
    suggestions.forEach((item, index) => {
        item.classList.toggle('highlighted', index === currentHighlight);
    });
}

// Click outside to close suggestions
document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-container')) {
        hideSuggestions();
    }
});

// Filter buttons
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Update active button
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        
        // Update filter
        currentFilter = button.dataset.category;
        
        // Re-search with new filter
        const query = searchInput.value;
        if (query.trim()) {
            showSuggestions(query);
            performSearch(query);
        }
    });
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    searchInput.focus();
    updateStats(0, searchData.length);
});