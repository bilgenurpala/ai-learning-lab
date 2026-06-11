import os

def create_ml_workflow_svg(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 130" width="100%" height="100%">
  <defs>
    <linearGradient id="ml-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="accent-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="100%" stop-color="#8B5CF6" />
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#64748B"/>
    </marker>
  </defs>
  
  <!-- Background -->
  <rect width="920" height="130" rx="12" fill="url(#ml-grad)" stroke="#334155" stroke-width="1.5" />
  
  <!-- Steps -->
  <!-- Step 1 -->
  <g transform="translate(15, 25)">
    <rect width="120" height="70" rx="8" fill="#1E293B" stroke="#3B82F6" stroke-width="1.5" />
    <text x="60" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Data Collection</text>
    <text x="60" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Raw Logs &amp; CSvs</text>
  </g>
  <line x1="135" y1="60" x2="160" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />
  
  <!-- Step 2 -->
  <g transform="translate(165, 25)">
    <rect width="120" height="70" rx="8" fill="#1E293B" stroke="#6366F1" stroke-width="1.5" />
    <text x="60" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Preprocessing</text>
    <text x="60" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Imputation &amp; Scale</text>
  </g>
  <line x1="285" y1="60" x2="310" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 3 -->
  <g transform="translate(315, 25)">
    <rect width="120" height="70" rx="8" fill="#1E293B" stroke="#8B5CF6" stroke-width="1.5" />
    <text x="60" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Feature Eng.</text>
    <text x="60" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Selection &amp; PCA</text>
  </g>
  <line x1="435" y1="60" x2="460" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 4 -->
  <g transform="translate(465, 25)">
    <rect width="120" height="70" rx="8" fill="#1E293B" stroke="#D946EF" stroke-width="1.5" />
    <text x="60" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Model Training</text>
    <text x="60" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Fit Scikit-learn</text>
  </g>
  <line x1="585" y1="60" x2="610" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 5 -->
  <g transform="translate(615, 25)">
    <rect width="120" height="70" rx="8" fill="#1E293B" stroke="#EC4899" stroke-width="1.5" />
    <text x="60" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Evaluation</text>
    <text x="60" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Inertia &amp; Metrics</text>
  </g>
  <line x1="735" y1="60" x2="760" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 6 -->
  <g transform="translate(765, 25)">
    <rect width="140" height="70" rx="8" fill="url(#ml-grad)" stroke="url(#accent-grad)" stroke-width="2" />
    <text x="70" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Model Deployment</text>
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#10B981" text-anchor="middle">FastAPI Microservice</text>
  </g>
</svg>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

def create_deep_learning_flow_svg(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="dl-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#64748B"/>
    </marker>
  </defs>
  
  <!-- Background -->
  <rect width="920" height="180" rx="12" fill="url(#dl-grad)" stroke="#334155" stroke-width="1.5" />
  
  <!-- Forward Pass Pipeline -->
  <!-- Input Node -->
  <g transform="translate(30, 50)">
    <circle cx="30" cy="30" r="25" fill="#1E293B" stroke="#3B82F6" stroke-width="2" />
    <text x="30" y="35" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#F8FAFC" text-anchor="middle">X</text>
    <text x="30" y="-10" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">Input Data</text>
  </g>
  <line x1="85" y1="80" x2="145" y2="80" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />
  
  <!-- Linear Combination -->
  <g transform="translate(150, 40)">
    <rect width="150" height="80" rx="8" fill="#1E293B" stroke="#8B5CF6" stroke-width="2" />
    <text x="75" y="35" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Linear Layer</text>
    <text x="75" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#D8B4FE" text-anchor="middle">z = wᵀx + b</text>
    <text x="75" y="-15" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">Weights &amp; Biases</text>
  </g>
  <line x1="300" y1="80" x2="355" y2="80" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />
  
  <!-- Activation Function -->
  <g transform="translate(360, 40)">
    <rect width="160" height="80" rx="8" fill="#1E293B" stroke="#EC4899" stroke-width="2" />
    <text x="80" y="35" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Activation Function</text>
    <text x="80" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FBCFE8" text-anchor="middle">a = g(z)</text>
    <text x="80" y="-15" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">ReLU / Sigmoid / Softmax</text>
  </g>
  <line x1="520" y1="80" x2="575" y2="80" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Output Prediction -->
  <g transform="translate(580, 50)">
    <circle cx="30" cy="30" r="25" fill="#1E293B" stroke="#10B981" stroke-width="2" />
    <text x="30" y="35" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" fill="#F8FAFC" text-anchor="middle">ŷ</text>
    <text x="30" y="-10" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">Prediction</text>
  </g>
  <line x1="640" y1="80" x2="695" y2="80" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Loss Computation -->
  <g transform="translate(700, 40)">
    <rect width="180" height="80" rx="8" fill="#1E293B" stroke="#EF4444" stroke-width="2" />
    <text x="90" y="35" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Loss Calculation</text>
    <text x="90" y="58" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FCA5A5" text-anchor="middle">ℒ(ŷ, y)</text>
    <text x="90" y="-15" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">Compute Error</text>
  </g>

  <!-- Backpropagation Loop -->
  <path d="M 790,120 C 790,170, 225,170, 225,125" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="5,5" marker-end="url(#arrow)" />
  <text x="500" y="155" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#F59E0B" text-anchor="middle">Backpropagation &amp; Gradient Updates: θₜ₊₁ = θₜ - η∇ℒ(θₜ)</text>
</svg>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

def create_cybersecurity_sec_ops_svg(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 130" width="100%" height="100%">
  <defs>
    <linearGradient id="cyber-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="alert-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EF4444" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#64748B"/>
    </marker>
  </defs>
  
  <!-- Background -->
  <rect width="920" height="130" rx="12" fill="url(#cyber-grad)" stroke="#334155" stroke-width="1.5" />
  
  <!-- Flow -->
  <!-- Step 1 -->
  <g transform="translate(20, 25)">
    <rect width="140" height="70" rx="8" fill="#1E293B" stroke="#64748B" stroke-width="1.5" />
    <text x="70" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Raw Cyber Logs</text>
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Syslog / PCAPs / Auth</text>
  </g>
  <line x1="160" y1="60" x2="195" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />
  
  <!-- Step 2 -->
  <g transform="translate(200, 25)">
    <rect width="140" height="70" rx="8" fill="#1E293B" stroke="#3B82F6" stroke-width="1.5" />
    <text x="70" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Log Parsing</text>
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Python Regex / JSON</text>
  </g>
  <line x1="340" y1="60" x2="375" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 3 -->
  <g transform="translate(380, 25)">
    <rect width="150" height="70" rx="8" fill="#1E293B" stroke="#8B5CF6" stroke-width="1.5" />
    <text x="75" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Feature Vectorization</text>
    <text x="75" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">IPs, Ports, Rates, Sizes</text>
  </g>
  <line x1="530" y1="60" x2="565" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 4 -->
  <g transform="translate(570, 25)">
    <rect width="150" height="70" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5" />
    <text x="75" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">ML Anomaly Model</text>
    <text x="75" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#A7F3D0" text-anchor="middle">Decision Tree / K-Means</text>
  </g>
  <line x1="720" y1="60" x2="755" y2="60" stroke="#64748B" stroke-width="2" marker-end="url(#arrow)" />

  <!-- Step 5 -->
  <g transform="translate(760, 25)">
    <rect width="140" height="70" rx="8" fill="url(#cyber-grad)" stroke="url(#alert-grad)" stroke-width="2" />
    <text x="70" y="32" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Security Response</text>
    <text x="70" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#FCA5A5" text-anchor="middle">Block IP / Raise Alert</text>
  </g>
</svg>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

if __name__ == "__main__":
    assets_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Generating ml_workflow.svg...")
    create_ml_workflow_svg(os.path.join(assets_dir, "ml_workflow.svg"))
    
    print("Generating deep_learning_flow.svg...")
    create_deep_learning_flow_svg(os.path.join(assets_dir, "deep_learning_flow.svg"))
    
    print("Generating cybersecurity_sec_ops.svg...")
    create_cybersecurity_sec_ops_svg(os.path.join(assets_dir, "cybersecurity_sec_ops.svg"))
    
    print("All diagrams generated successfully!")
