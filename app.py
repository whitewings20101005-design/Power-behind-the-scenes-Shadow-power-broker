import streamlit as st
import google.generativeai as genai

# 1. サイトのデザインとタイトル設定
st.set_page_config(page_title="みんなの健康レシピ考案機", page_icon="🥗", layout="centered")

st.title("🥗 パーソナル健康レシピ考案システム")
st.write("条件を選んでボタンを押すだけで、この場で即座に完璧な健康レシピを考案します！")

st.write("---")

# 2. ユーザーがサイト上で選ぶ入力フォーム
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("👤 性別を選んでください", ["男性", "女性", "その他"])
    age = st.number_input("🎂 年齢を入力してください", min_value=1, max_value=100, value=18)

with col2:
    purpose = st.selectbox("🎯 目的を選んでください", ["健康維持（バランス）", "ダイエット（低カロリー）", "筋トレ（高タンパク）"])
    meal_time = st.selectbox("⏰ 食事のタイミング", ["朝食", "昼食（お弁当）", "夕食", "間食"])

# 3. 食材の入力欄
st.subheader("🛒 今手元にある食材（使いたい食材）")
user_ingredients = st.text_input("例：冷凍ブロッコリー, 鶏肉, 卵", "冷凍ブロッコリー, 鶏肉")

st.write("---")

# 4. ボタンを押したらその場でレシピを生成・表示
if st.button("✨ この食材で健康レシピを検索・考案する"):
    
    with st.spinner("🧠 AI管理栄養士がレシピを考えています...（約10秒かかります）"):
        
        # AIへ送るプロンプトの文章
        prompt_text = f"ユーザー条件：{age}歳 {gender}、目的：{purpose}、タイミング：{meal_time}。食材：{user_ingredients}。これらを使って、健康的で美味しいレシピを1品考案してください。出力形式は「■ 考案メニュー名」「■ 必要な食材とグラム数」「■ 作り方」「■ 推定栄養価（カロリー、PFC）」「■ 栄養アドバイス」の5項目で、全て日本語で分かりやすく出力してください。"
        
        try:
            # 🌟 18歳以下でも設定なしで使える無料モデルを呼び出し
            # 特殊なキー（秘密鍵）はStreamlitの画面側で後ほど1発入力します！
            if "GEMINI_API_KEY" in st.secrets:
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            elif "gemini_api_key" in st.secrets:
                genai.configure(api_key=st.secrets["gemini_api_key"])
            else:
                st.error("🔑 サイトの管理画面でAIの鍵（GEMINI_API_KEY）が設定されていません。")
                st.stop()
                
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt_text)
            
            # 画面に直接結果を表示！
            st.success("🎉 レシピが完成しました！")
            st.markdown(response.text)
                
        except Exception as e:
            st.error("⚠️ レシピの自動生成中にエラーが発生しました。時間を置いて再度お試しください。")
