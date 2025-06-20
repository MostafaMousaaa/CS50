let watchId = null;
let locationHistory = [];

function checkGeolocationSupport() {
    if (!navigator.geolocation) {
        showStatus('Geolocation is not supported by this browser.', 'error');
        return false;
    }
    return true;
}

function getCurrentLocation() {
    if (!checkGeolocationSupport()) return;

    const options = getLocationOptions();
    
    showStatus('🔍 Getting your location...', 'loading');
    document.getElementById('getLocationBtn').disabled = true;

    navigator.geolocation.getCurrentPosition(
        (position) => {
            displayLocation(position);
            addToHistory(position, 'Single request');
            showStatus('✅ Location found successfully!', 'success');
            document.getElementById('getLocationBtn').disabled = false;
        },
        (error) => {
            handleLocationError(error);
            document.getElementById('getLocationBtn').disabled = false;
        },
        options
    );
}

function watchLocation() {
    if (!checkGeolocationSupport()) return;

    const options = getLocationOptions();
    
    showStatus('👀 Watching for location changes...', 'loading');
    document.getElementById('watchLocationBtn').disabled = true;
    document.getElementById('stopWatchBtn').disabled = false;

    watchId = navigator.geolocation.watchPosition(
        (position) => {
            displayLocation(position);
            addToHistory(position, 'Continuous watch');
            showStatus('📍 Location updated!', 'success');
        },
        (error) => {
            handleLocationError(error);
        },
        options
    );
}

function stopWatching() {
    if (watchId !== null) {
        navigator.geolocation.clearWatch(watchId);
        watchId = null;
        showStatus('⏹️ Stopped watching location', 'success');
        document.getElementById('watchLocationBtn').disabled = false;
        document.getElementById('stopWatchBtn').disabled = true;
    }
}

function getLocationOptions() {
    return {
        enableHighAccuracy: document.getElementById('enableHighAccuracy').checked,
        timeout: parseInt(document.getElementById('timeout').value),
        maximumAge: parseInt(document.getElementById('maximumAge').value)
    };
}

function displayLocation(position) {
    const coords = position.coords;
    
    // Show results section
    document.getElementById('locationResults').style.display = 'block';
    
    // Basic information
    document.getElementById('latitude').textContent = coords.latitude.toFixed(6);
    document.getElementById('longitude').textContent = coords.longitude.toFixed(6);
    document.getElementById('accuracy').textContent = coords.accuracy ? `±${coords.accuracy.toFixed(1)} meters` : 'Unknown';
    document.getElementById('timestamp').textContent = new Date(position.timestamp).toLocaleString();
    
    // Detailed data
    document.getElementById('altitude').textContent = coords.altitude ? `${coords.altitude.toFixed(1)} meters` : 'Not available';
    document.getElementById('altitudeAccuracy').textContent = coords.altitudeAccuracy ? `±${coords.altitudeAccuracy.toFixed(1)} meters` : 'Not available';
    document.getElementById('heading').textContent = coords.heading ? `${coords.heading.toFixed(1)}°` : 'Not available';
    document.getElementById('speed').textContent = coords.speed ? `${coords.speed.toFixed(1)} m/s` : 'Not available';
    
    // Technical details
    document.getElementById('coordinates').textContent = `${coords.latitude}, ${coords.longitude}`;
    
    // Accuracy level
    const accuracyLevel = getAccuracyLevel(coords.accuracy);
    const accuracyElement = document.getElementById('accuracyLevel');
    accuracyElement.textContent = accuracyLevel.text;
    accuracyElement.className = `accuracy-indicator ${accuracyLevel.class}`;
    
    // Update map placeholder
    updateMapPlaceholder(coords);
    
    // Show weather widget (simulated)
    showWeatherInfo(coords);
}

function getAccuracyLevel(accuracy) {
    if (!accuracy) return { text: 'Unknown', class: 'accuracy-low' };
    
    if (accuracy <= 10) return { text: 'Very High', class: 'accuracy-high' };
    if (accuracy <= 50) return { text: 'High', class: 'accuracy-high' };
    if (accuracy <= 100) return { text: 'Medium', class: 'accuracy-medium' };
    return { text: 'Low', class: 'accuracy-low' };
}

function updateMapPlaceholder(coords) {
    const mapElement = document.getElementById('mapPlaceholder');
    mapElement.innerHTML = `
        🗺️ Your location on map<br>
        <small>Lat: ${coords.latitude.toFixed(4)}, Lng: ${coords.longitude.toFixed(4)}</small><br>
        <small>Accuracy: ±${coords.accuracy ? coords.accuracy.toFixed(1) : '?'} meters</small>
    `;
}

function showWeatherInfo(coords) {
    const weatherWidget = document.getElementById('weatherWidget');
    weatherWidget.style.display = 'block';
    
    // Simulate weather data based on location
    const mockTemp = Math.round(20 + Math.random() * 15);
    const conditions = ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain'][Math.floor(Math.random() * 4)];
    
    document.getElementById('temperature').textContent = `${mockTemp}°C`;
    document.getElementById('conditions').textContent = conditions;
}

function handleLocationError(error) {
    let errorMessage = '';
    
    switch (error.code) {
        case error.PERMISSION_DENIED:
            errorMessage = '🚫 Location access denied by user. Please enable location services and refresh the page.';
            break;
        case error.POSITION_UNAVAILABLE:
            errorMessage = '📍 Location information is unavailable. Please check your device settings.';
            break;
        case error.TIMEOUT:
            errorMessage = '⏰ Location request timed out. Please try again.';
            break;
        default:
            errorMessage = '❌ An unknown error occurred while retrieving location.';
            break;
    }
    
    showStatus(errorMessage, 'error');
    console.error('Geolocation error:', error);
}

function showStatus(message, type) {
    const statusElement = document.getElementById('locationStatus');
    statusElement.textContent = message;
    statusElement.className = `status ${type}`;
}

function addToHistory(position, source) {
    const coords = position.coords;
    const historyItem = {
        timestamp: position.timestamp,
        latitude: coords.latitude,
        longitude: coords.longitude,
        accuracy: coords.accuracy,
        source: source
    };
    
    locationHistory.unshift(historyItem);
    
    // Keep only last 10 entries
    if (locationHistory.length > 10) {
        locationHistory = locationHistory.slice(0, 10);
    }
    
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    const historyElement = document.getElementById('locationHistory');
    
    if (locationHistory.length === 0) {
        historyElement.innerHTML = '<p>No location history yet.</p>';
        return;
    }
    
    historyElement.innerHTML = locationHistory
        .map((item, index) => `
            <div class="info-card">
                <h5>#${index + 1} - ${item.source}</h5>
                <p><strong>Time:</strong> ${new Date(item.timestamp).toLocaleString()}</p>
                <p><strong>Coordinates:</strong> ${item.latitude.toFixed(6)}, ${item.longitude.toFixed(6)}</p>
                <p><strong>Accuracy:</strong> ±${item.accuracy ? item.accuracy.toFixed(1) : '?'} meters</p>
            </div>
        `).join('');
}

function clearHistory() {
    locationHistory = [];
    updateHistoryDisplay();
    showStatus('🗑️ Location history cleared', 'success');
}

// Demonstrate location features on page load
document.addEventListener('DOMContentLoaded', () => {
    if (navigator.geolocation) {
        showStatus('🌍 Geolocation API is available. Click "Get Current Location" to start.', 'success');
    } else {
        showStatus('❌ Geolocation API is not supported by this browser.', 'error');
    }
    
    updateHistoryDisplay();
});

// Demonstrate geolocation capabilities check
function demonstrateCapabilities() {
    console.log('Geolocation capabilities:');
    console.log('- getCurrentPosition:', typeof navigator.geolocation?.getCurrentPosition === 'function');
    console.log('- watchPosition:', typeof navigator.geolocation?.watchPosition === 'function');
    console.log('- clearWatch:', typeof navigator.geolocation?.clearWatch === 'function');
    
    // Check for additional APIs that work well with geolocation
    console.log('- Battery API:', 'getBattery' in navigator);
    console.log('- Network Information:', 'connection' in navigator);
    console.log('- Device Orientation:', 'DeviceOrientationEvent' in window);
}

// Run capability check
demonstrateCapabilities();