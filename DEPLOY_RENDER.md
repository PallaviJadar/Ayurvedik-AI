# Deploy to Render.com (FREE)

## Step 1: Create a Render Account
1. Go to [https://render.com](https://render.com)
2. Sign up for free using your GitHub account (recommended) or email

## Step 2: Push Your Code to GitHub
1. Create a new repository on GitHub (if you haven't already)
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

## Step 3: Deploy on Render
1. Log into [https://dashboard.render.com](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `ayurvedic-ai` (or any name you like)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Instance Type**: Free

## Step 4: Add Environment Variables
1. In the Render dashboard, go to your service's **"Environment"** tab
2. Click **"Add Environment Variable"**
3. Add:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your actual Gemini API key (paste the full key)
4. Click **"Save Changes"**

## Step 5: Deploy
1. Render will automatically start building and deploying your app
2. Wait for the build to complete (usually 3-5 minutes)
3. Once it shows "Live", click on the URL to access your app!

## Important Notes
- **First deployment** takes longer (downloading dependencies)
- **Free tier** sleeps after 15 minutes of inactivity (takes 30 seconds to wake up)
- Your app will be accessible at: `https://ayurvedic-ai-XXXX.onrender.com`

## Troubleshooting
- If the app doesn't start, check the **"Logs"** tab for errors
- Make sure `GEMINI_API_KEY` is set correctly in Environment Variables
- The app should work immediately after deployment!
