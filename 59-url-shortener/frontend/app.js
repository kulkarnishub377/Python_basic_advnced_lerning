/**
 * app.js - Frontend logic for URL Shortener
 */

const API_BASE = 'http://127.0.0.1:8000/api';

const form = document.getElementById('shorten-form');
const urlInput = document.getElementById('url-input');
const resultArea = document.getElementById('result-area');
const shortUrlDisplay = document.getElementById('short-url-display');
const btnCopy = document.getElementById('btn-copy');
const errorMsg = document.getElementById('error-message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Reset UI
    resultArea.classList.add('hidden');
    errorMsg.classList.add('hidden');
    
    const longUrl = urlInput.value.trim();
    if (!longUrl) return;

    try {
        const response = await fetch(`${API_BASE}/shorten`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: longUrl })
        });

        const data = await response.json();

        if (response.ok) {
            // Show success
            shortUrlDisplay.textContent = data.short_url;
            shortUrlDisplay.href = data.short_url;
            resultArea.classList.remove('hidden');
            
            // Clear input
            urlInput.value = '';
        } else {
            // Show validation error (e.g. invalid URL format)
            errorMsg.textContent = data.detail[0]?.msg || JSON.stringify(data.detail);
            errorMsg.classList.remove('hidden');
        }

    } catch (err) {
        console.error(err);
        errorMsg.textContent = "Failed to connect to the server. Is the backend running?";
        errorMsg.classList.remove('hidden');
    }
});

btnCopy.addEventListener('click', async () => {
    const textToCopy = shortUrlDisplay.textContent;
    try {
        await navigator.clipboard.writeText(textToCopy);
        
        // Visual feedback
        const icon = btnCopy.querySelector('i');
        icon.className = 'fa-solid fa-check';
        icon.style.color = '#34d399';
        
        setTimeout(() => {
            icon.className = 'fa-regular fa-copy';
            icon.style.color = '';
        }, 2000);
    } catch (err) {
        console.error('Failed to copy text: ', err);
    }
});
