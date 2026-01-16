// VisCar SDV GenAI Generator - Interactive Demo JavaScript

// ============================================================================
// Vehicle Telemetry Simulation
// ============================================================================

class VehicleTelemetry {
    constructor() {
        this.isRunning = false;
        this.speed = 0;
        this.battery = 85;
        this.tyrePressure = [32, 32, 32, 32]; // FL, FR, RL, RR
        this.evRange = 420;
        this.diagnostics = [];
        this.predictions = [];
    }

    start() {
        this.isRunning = true;
        this.simulate();
    }

    simulate() {
        if (!this.isRunning) return;

        // Simulate speed variations
        this.speed = 60 + Math.sin(Date.now() / 2000) * 20 + Math.random() * 10;
        document.getElementById('speed').textContent = Math.round(this.speed);

        // Simulate battery discharge
        this.battery = Math.max(20, 85 - (Date.now() % 100000) / 1500);
        document.getElementById('battery').textContent = Math.round(this.battery);

        // Simulate tyre pressure variations
        this.tyrePressure = this.tyrePressure.map(p =>
            32 + (Math.random() - 0.5) * 2
        );
        document.getElementById('tyreFL').textContent = this.tyrePressure[0].toFixed(1);
        document.getElementById('tyreFR').textContent = this.tyrePressure[1].toFixed(1);
        document.getElementById('tyreRL').textContent = this.tyrePressure[2].toFixed(1);
        document.getElementById('tyreRR').textContent = this.tyrePressure[3].toFixed(1);

        const avgPressure = this.tyrePressure.reduce((a, b) => a + b) / 4;
        document.getElementById('tyrePressure').textContent = avgPressure.toFixed(1);

        // Simulate EV range
        this.evRange = Math.max(50, 420 - (Date.now() % 100000) / 250);
        document.getElementById('evRange').textContent = Math.round(this.evRange);

        // Update diagnostics
        this.updateDiagnostics();

        // Update predictions
        this.updatePredictions();

        setTimeout(() => this.simulate(), 1000);
    }

    updateDiagnostics() {
        const diagnosticsList = document.getElementById('diagnosticsList');

        // Clear existing
        diagnosticsList.innerHTML = '';

        // Check for issues
        const issues = [];

        if (this.battery < 30) {
            issues.push({
                status: 'warning',
                message: 'Low Battery Warning - Consider Charging'
            });
        }

        const lowPressure = this.tyrePressure.some(p => p < 30);
        if (lowPressure) {
            issues.push({
                status: 'warning',
                message: 'Low Tyre Pressure Detected'
            });
        }

        if (issues.length === 0) {
            diagnosticsList.innerHTML = `
                <div class="diagnostic-item status-ok">
                    <span class="status-indicator"></span>
                    <span>All Systems Operational</span>
                </div>
            `;
        } else {
            issues.forEach(issue => {
                const item = document.createElement('div');
                item.className = `diagnostic-item status-${issue.status}`;
                item.innerHTML = `
                    <span class="status-indicator"></span>
                    <span>${issue.message}</span>
                `;
                diagnosticsList.appendChild(item);
            });
        }
    }

    updatePredictions() {
        const predictionsList = document.getElementById('predictionsList');

        predictionsList.innerHTML = `
            <div class="prediction-item">
                <strong>Battery Health:</strong>
                <span>${(this.battery * 1.05).toFixed(1)}%</span>
            </div>
            <div class="prediction-item">
                <strong>Brake Pad Life:</strong>
                <span>12,500 km remaining</span>
            </div>
            <div class="prediction-item">
                <strong>Next Service:</strong>
                <span>In 45 days</span>
            </div>
            <div class="prediction-item">
                <strong>Component Risk Score:</strong>
                <span>Low (15/100)</span>
            </div>
        `;
    }
}

// ============================================================================
// OTA Injection Simulation
// ============================================================================

class OTAManager {
    constructor() {
        this.services = [
            { name: 'VehicleDataService', language: 'C++', injected: false },
            { name: 'DiagnosticsService', language: 'C++', injected: false },
            { name: 'AnalyticsService', language: 'Rust', injected: false },
            { name: 'PredictionService', language: 'Rust', injected: false },
            { name: 'OTAFeatureService', language: 'C++', injected: false }
        ];
        this.otaInjected = false;
    }

    renderServices() {
        const registry = document.getElementById('serviceRegistry');
        registry.innerHTML = '';

        this.services.forEach(service => {
            const box = document.createElement('div');
            box.className = 'service-box' + (service.injected ? ' injected' : '');
            box.innerHTML = `
                <strong>${service.name}</strong>
                <span>${service.language}</span>
            `;
            registry.appendChild(box);
        });
    }

    async injectService() {
        if (this.otaInjected) {
            this.addLogEntry('OTA service already injected', 'info');
            return;
        }

        const log = document.getElementById('otaLog');
        const btn = document.getElementById('injectOtaBtn');

        btn.disabled = true;
        btn.textContent = 'Injecting...';

        // Simulation steps
        const steps = [
            'Connecting to OTA server...',
            'Authenticating vehicle identity...',
            'Downloading BatteryDegradationService package...',
            'Validating package signature...',
            'Checking dependencies (VehicleDataService, AnalyticsService)...',
            'Dependencies satisfied ✓',
            'Generating service code...',
            'Compiling Rust service...',
            'Running MISRA compliance checks...',
            'Generating unit tests...',
            'Updating service registry...',
            'Registering service endpoints...',
            'BatteryDegradationService injected successfully! ✓'
        ];

        for (let i = 0; i < steps.length; i++) {
            await this.sleep(400);
            const className = i === steps.length - 1 ? 'success' : 'info';
            this.addLogEntry(steps[i], className);

            if (log.scrollHeight > log.clientHeight) {
                log.scrollTop = log.scrollHeight;
            }
        }

        // Add the new service
        this.services.push({
            name: 'BatteryDegradationService',
            language: 'Rust',
            injected: true
        });

        this.otaInjected = true;
        this.renderServices();

        btn.textContent = '✓ Service Injected';
        btn.style.background = 'linear-gradient(135deg, hsl(140, 70%, 50%), hsl(140, 70%, 40%))';
    }

    addLogEntry(message, className = '') {
        const log = document.getElementById('otaLog');
        const entry = document.createElement('div');
        entry.className = 'log-entry ' + className;
        entry.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
        log.appendChild(entry);
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// ============================================================================
// Chart Rendering
// ============================================================================

class MiniChart {
    constructor(elementId, color) {
        this.element = document.getElementById(elementId);
        this.color = color;
        this.dataPoints = [];
        this.maxPoints = 20;
    }

    addPoint(value) {
        this.dataPoints.push(value);
        if (this.dataPoints.length > this.maxPoints) {
            this.dataPoints.shift();
        }
        this.render();
    }

    render() {
        if (!this.element) return;

        const max = Math.max(...this.dataPoints, 1);
        const min = Math.min(...this.dataPoints, 0);
        const range = max - min || 1;

        const width = this.element.clientWidth;
        const height = this.element.clientHeight;
        const stepX = width / (this.maxPoints - 1);

        let path = '';
        this.dataPoints.forEach((value, index) => {
            const x = index * stepX;
            const y = height - ((value - min) / range * height);
            path += (index === 0 ? 'M' : 'L') + x + ' ' + y + ' ';
        });

        this.element.innerHTML = `
            <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0;">
                <defs>
                    <linearGradient id="gradient-${elementId}" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" style="stop-color:${this.color};stop-opacity:0.3" />
                        <stop offset="100%" style="stop-color:${this.color};stop-opacity:0" />
                    </linearGradient>
                </defs>
                <path d="${path} L${width} ${height} L0 ${height} Z" 
                      fill="url(#gradient-${elementId})" />
                <path d="${path}" 
                      stroke="${this.color}" 
                      stroke-width="2" 
                      fill="none" />
            </svg>
        `;
    }
}

// ============================================================================
// Initialization
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    // Initialize telemetry
    const telemetry = new VehicleTelemetry();
    telemetry.start();

    // Initialize OTA manager
    const otaManager = new OTAManager();
    otaManager.renderServices();

    // Set up OTA injection button
    const otaBtn = document.getElementById('injectOtaBtn');
    if (otaBtn) {
        otaBtn.addEventListener('click', () => {
            otaManager.injectService();
        });
    }

    // Initialize charts
    const speedChart = new MiniChart('speedChart', 'hsl(210, 100%, 60%)');
    const batteryChart = new MiniChart('batteryChart', 'hsl(140, 70%, 50%)');
    const rangeChart = new MiniChart('rangeChart', 'hsl(280, 100%, 65%)');

    // Update charts periodically
    setInterval(() => {
        speedChart.addPoint(telemetry.speed);
        batteryChart.addPoint(telemetry.battery);
        rangeChart.addPoint(telemetry.evRange / 10); // Scale down for chart
    }, 1000);

    // Smooth scroll for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add scroll-based animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Animate sections on scroll
    document.querySelectorAll('.section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });

    // Log startup message
    console.log('%c🚗 VisCar SDV GenAI Generator', 'font-size: 20px; font-weight: bold; color: #3b82f6;');
    console.log('%cDemonstration running...', 'font-size: 14px; color: #9ca3af;');
    console.log('%c→ Vehicle telemetry simulation active', 'color: #10b981;');
    console.log('%c→ OTA injection ready', 'color: #10b981;');
    console.log('%c→ Real-time diagnostics enabled', 'color: #10b981;');
});

// Tyre pressure color coding
setInterval(() => {
    const tyres = ['tyreFL', 'tyreFR', 'tyreRL', 'tyreRR'];
    tyres.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            const pressure = parseFloat(element.textContent);
            if (pressure < 30) {
                element.style.background = 'hsl(0, 80%, 30%)';
                element.style.color = 'hsl(0, 80%, 70%)';
            } else if (pressure > 34) {
                element.style.background = 'hsl(40, 100%, 30%)';
                element.style.color = 'hsl(40, 100%, 70%)';
            } else {
                element.style.background = 'var(--bg-secondary)';
                element.style.color = 'var(--text-primary)';
            }
        }
    });
}, 1000);
