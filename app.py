import streamlit as st
import urllib.request
import json

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
    
    with st.spinner("🧠 AI管理栄養士がレシピを考えています...（約10〜20秒かかります）"):
        
        # AIへ送るプロンプトの文章
        prompt_text = f"ユーザー条件：{age}歳 {gender}、目的：{purpose}、タイミング：{meal_time}。食材：{user_ingredients}。これらを使って、健康的で美味しいレシピを1品考案してください。出力形式は「■ 考案メニュー名」「■ 必要な食材とグラム数」「■ 作り方」「■ 推定栄養価（カロリー、PFC）」「■ 栄養アドバイス」の5項目で、全て日本語で分かりやすく出力してください。"
        
        try:
            # 💡 修正箇所：自分専用のトークンを使ってAIを呼び出す
            HF_TOKEN = "hf_...ccwA"
            
            url = "https://huggingface.co"
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {HF_TOKEN}"
            }
            
            data = {
                "inputs": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{prompt_text}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
                "parameters": {"max_new_tokens": 1024, "temperature": 0.7}
            }
            
            req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
            
            with urllib.request.urlopen(req) as res:
                result = json.loads(res.read().decode("utf-8"))
                output_text = result["generated_text"].split("<|start_header_id|>assistant<|end_header_id|>\n\n")[-1]
                
                # 画面に直接結果を表示！
                st.success("🎉 レシピが完成しました！")
                st.markdown(output_text)
                
        except Exception as e:
            st.error("⚠️ レシピの自動生成中にエラーが発生しました。トークンが正しいか確認し、時間を置いて再度お試しください。")
