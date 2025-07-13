// Regular expression patterns
const patterns = {
    email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
    phone: /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/,
    name: /^[a-zA-Z\s]{2,50}$/,
    website: /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/,
    strongPassword: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/
};

// Form elements
const form = document.getElementById('validationForm');
const submitBtn = document.getElementById('submitBtn');
const fields = {
    name: document.getElementById('name'),
    email: document.getElementById('email'),
    phone: document.getElementById('phone'),
    password: document.getElementById('password'),
    confirmPassword: document.getElementById('confirmPassword'),
    age: document.getElementById('age'),
    website: document.getElementById('website'),
    comments: document.getElementById('comments')
};

// Validation state
const validationState = {
    name: false,
    email: false,
    phone: false,
    password: false,
    confirmPassword: false,
    age: false,
    website: true // Optional field
};

// Validation functions
function validateField(fieldName, value, isRequired = true) {
    const field = fields[fieldName];
    const errorDiv = document.getElementById(fieldName + 'Error');
    const successDiv = document.getElementById(fieldName + 'Success');
    
    // Clear previous states
    field.classList.remove('error', 'success');
    errorDiv.style.display = 'none';
    successDiv.style.display = 'none';
    
    // Skip validation for empty optional fields
    if (!isRequired && !value.trim()) {
        validationState[fieldName] = true;
        return true;
    }
    
    // Required field check
    if (isRequired && !value.trim()) {
        showError(field, errorDiv, 'This field is required');
        validationState[fieldName] = false;
        return false;
    }
    
    let isValid = true;
    let errorMessage = '';
    
    switch (fieldName) {
        case 'name':
            if (!patterns.name.test(value)) {
                errorMessage = 'Name must be 2-50 characters and contain only letters and spaces';
                isValid = false;
            }
            break;
            
        case 'email':
            if (!patterns.email.test(value)) {
                errorMessage = 'Please enter a valid email address';
                isValid = false;
            }
            break;
            
        case 'phone':
            if (!patterns.phone.test(value)) {
                errorMessage = 'Please enter a valid phone number (e.g., (123) 456-7890)';
                isValid = false;
            }
            break;
            
        case 'password':
            const strength = getPasswordStrength(value);
            updatePasswordStrength(strength);
            
            if (value.length < 8) {
                errorMessage = 'Password must be at least 8 characters long';
                isValid = false;
            } else if (strength < 3) {
                errorMessage = 'Password must contain uppercase, lowercase, number, and special character';
                isValid = false;
            }
            break;
            
        case 'confirmPassword':
            if (value !== fields.password.value) {
                errorMessage = 'Passwords do not match';
                isValid = false;
            }
            break;
            
        case 'age':
            const age = parseInt(value);
            if (isNaN(age) || age < 13 || age > 120) {
                errorMessage = 'Age must be between 13 and 120';
                isValid = false;
            }
            break;
            
        case 'website':
            if (value.trim() && !patterns.website.test(value)) {
                errorMessage = 'Please enter a valid URL (include http:// or https://)';
                isValid = false;
            }
            break;
    }
    
    if (isValid) {
        showSuccess(field, successDiv);
        validationState[fieldName] = true;
    } else {
        showError(field, errorDiv, errorMessage);
        validationState[fieldName] = false;
    }
    
    updateSubmitButton();
    return isValid;
}

function showError(field, errorDiv, message) {
    field.classList.add('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function showSuccess(field, successDiv) {
    field.classList.add('success');
    successDiv.style.display = 'block';
}

function getPasswordStrength(password) {
    let strength = 0;
    
    // Length check
    if (password.length >= 8) strength++;
    if (password.length >= 12) strength++;
    
    // Character type checks
    if (/[a-z]/.test(password)) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[@$!%*?&]/.test(password)) strength++;
    
    return Math.min(strength, 4);
}

function updatePasswordStrength(strength) {
    const strengthBar = document.getElementById('strengthBar');
    const percentage = (strength / 4) * 100;
    
    strengthBar.style.width = percentage + '%';
    
    if (strength <= 1) {
        strengthBar.className = 'strength-bar weak';
    } else if (strength <= 2) {
        strengthBar.className = 'strength-bar medium';
    } else {
        strengthBar.className = 'strength-bar strong';
    }
}

function updateSubmitButton() {
    const allValid = Object.values(validationState).every(Boolean);
    submitBtn.disabled = !allValid;
}

function updateCharacterCount() {
    const comments = fields.comments.value;
    const count = comments.length;
    const countDiv = document.getElementById('commentCount');
    countDiv.textContent = `${count}/500 characters`;
    
    if (count > 450) {
        countDiv.style.color = '#e74c3c';
    } else if (count > 400) {
        countDiv.style.color = '#f39c12';
    } else {
        countDiv.style.color = '#666';
    }
}

// Event listeners for real-time validation
fields.name.addEventListener('input', (e) => validateField('name', e.target.value));
fields.email.addEventListener('input', (e) => validateField('email', e.target.value));
fields.phone.addEventListener('input', (e) => validateField('phone', e.target.value));
fields.password.addEventListener('input', (e) => {
    validateField('password', e.target.value);
    // Re-validate confirm password if it has content
    if (fields.confirmPassword.value) {
        validateField('confirmPassword', fields.confirmPassword.value);
    }
});
fields.confirmPassword.addEventListener('input', (e) => validateField('confirmPassword', e.target.value));
fields.age.addEventListener('input', (e) => validateField('age', e.target.value));
fields.website.addEventListener('input', (e) => validateField('website', e.target.value, false));
fields.comments.addEventListener('input', updateCharacterCount);

// Form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Validate all fields
    let allValid = true;
    for (const [fieldName, field] of Object.entries(fields)) {
        if (fieldName === 'comments') continue;
        const isRequired = fieldName !== 'website';
        if (!validateField(fieldName, field.value, isRequired)) {
            allValid = false;
        }
    }
    
    if (allValid) {
        alert('✅ Form submitted successfully!\n\nIn a real application, this data would be sent to a server.');
        console.log('Form data:', new FormData(form));
    } else {
        alert('❌ Please fix the errors before submitting.');
    }
});

// Regular expression demo
function setupRegexDemo() {
    const regexInput = document.getElementById('regexInput');
    const phoneRegexInput = document.getElementById('phoneRegexInput');
    const passwordRegexInput = document.getElementById('passwordRegexInput');
    
    regexInput.addEventListener('input', (e) => {
        const result = document.getElementById('emailRegexResult');
        const isValid = patterns.email.test(e.target.value);
        result.textContent = isValid ? 'Valid' : 'Invalid';
        result.className = 'regex-result ' + (isValid ? 'match' : 'no-match');
    });
    
    phoneRegexInput.addEventListener('input', (e) => {
        const result = document.getElementById('phoneRegexResult');
        const isValid = patterns.phone.test(e.target.value);
        result.textContent = isValid ? 'Valid' : 'Invalid';
        result.className = 'regex-result ' + (isValid ? 'match' : 'no-match');
    });
    
    passwordRegexInput.addEventListener('input', (e) => {
        const result = document.getElementById('passwordRegexResult');
        const isValid = patterns.strongPassword.test(e.target.value);
        result.textContent = isValid ? 'Strong' : 'Weak';
        result.className = 'regex-result ' + (isValid ? 'match' : 'no-match');
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupRegexDemo();
    updateCharacterCount();
});