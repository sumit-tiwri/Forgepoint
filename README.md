# FORGEPOINT (SIH26136)
### AI-Powered Public Innovation-to-Scale Platform
> Problem Statement SIH26136: *Startup Friendly Public Procurement System*

---

## 🚀 Quick Start (Local Setup)

### Prerequisites
- **Node.js**: Version `18.x`, `20.x`, or `22.x` (LTS recommended). Check with `node -v`.
- **npm**: Version `9.x` or `10.x`. Check with `npm -v`.

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### Step 2: Install Dependencies
```bash
npm install
```

### Step 3: Configure Environment Variables (Optional)
Copy the example environment configuration:
```bash
cp .env.example .env
```
*(Note: An API key is **not required** to run the app. If `GEMINI_API_KEY` is not provided, the platform automatically runs using its high-fidelity deterministic innovation engine fallback).*

### Step 4: Run the Development Server
You have two options to run locally:

#### Option A: Full-Stack Mode (Express + Vite Proxy on Port 3000)
```bash
npm run dev
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser.

#### Option B: Client-Only Vite Mode (Fast Frontend on Port 5173 / 3000)
If you do not need the backend or port 3000 is occupied:
```bash
npm run dev:client
```
Open **[http://localhost:5173](http://localhost:5173)** in your browser.

---

## 🛠️ Production Build & Verification

To verify that the application compiles and builds for production:

```bash
# 1. Build optimized static bundle
npm run build

# 2. Test the production server locally
npm start
```
The production bundle will be generated in `./dist` and served on `http://localhost:3000`.

---

## 🌐 Hosting on GitHub & Cloud Platforms

### 1. GitHub Pages (Automated via GitHub Actions)
This repository includes an automated workflow file at `.github/workflows/deploy.yml`:
1. Push your code to your GitHub repository:
   ```bash
   git add .
   git commit -m "feat: complete FORGEPOINT platform"
   git push origin main
   ```
2. In your GitHub repository:
   - Go to **Settings** → **Pages** (in the left sidebar).
   - Under **Build and deployment** → **Source**, select **GitHub Actions**.
3. Once selected, GitHub will automatically run the build and deploy your site to:
   `https://<your-username>.github.io/<your-repo-name>/`

### 2. One-Click Deploy to Vercel
1. Import your GitHub repository into [Vercel](https://vercel.com).
2. Framework Preset: **Vite**
3. Build Command: `npm run build`
4. Output Directory: `dist`
5. Click **Deploy**.

### 3. Deploy to Render / Railway / Cloud Run (Full-Stack)
- **Build Command**: `npm install && npm run build`
- **Start Command**: `npm start`
- **Environment Variable**: `PORT=3000` (or host provided port).

---

## ❓ Troubleshooting Common Local Issues

| Issue | Cause | 1-Minute Fix |
|---|---|---|
| `command not found: tsx` | Dependencies not installed | Run `npm install` |
| `Error: listen EADDRINUSE :::3000` | Port 3000 is used by another process | Run `npm run dev:client` or change `PORT=3001 npm run dev` |
| Windows PowerShell: `running scripts is disabled` | Windows ExecutionPolicy restriction | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in PowerShell, then run `npm run dev` |
| GitHub Pages shows blank screen or 404 | Missing relative base path | `base: './'` has been pre-configured in `vite.config.ts`. Ensure GitHub Actions is set as source in repo settings. |
| Node version mismatch | Using older Node.js (<18) | Install Node 20 LTS from [nodejs.org](https://nodejs.org) or use `nvm use 20` |

---

## 🏛️ Platform Architecture & SIH26136 Features

- **Executive Bento Dashboard**: Comprehensive analytics (24 challenges, 186 startups, 12 active pilots, ₹1.85 Cr civic savings).
- **12-Step Guided Demo Tour**: One-click guided walkthrough for hackathon judges and evaluators.
- **5-Role Switcher**: Instant switching between Government Officer, Startup Innovator, Academic Expert, Youth Developer, and System Admin.
- **AI Challenge Builder**: Transforms unstructured civic problems into 15 procurement-ready structured fields (powered by Gemini 3.8 Flash + deterministic fallback).
- **Semantic Matching Engine**: Ranks DPIIT-recognized startups against challenge criteria with explainable reasoning.
- **Controlled Pilot Sandbox**: 90-day progress tracker with 6 milestones, telemetry convergence graphs, and risk mitigation logs.
- **Cryptographic Evidence Registry**: SHA-256 digests for all operational telemetry logs and fuel inspection reports.
- **Statutory Procurement Pathways**: Aligned with GeM Startup Runway (DPIIT exemption) and GFR Rule 194.
- **Verifiable Innovation Proof Dossier**: Tamper-evident printable certificates and QR codes preventing redundant trials.
- **Youth Innovation Hub**: Open challenge portal for students and developers to build verified portfolios.
