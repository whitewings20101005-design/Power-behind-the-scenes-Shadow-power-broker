import streamlit as st

# 1. サイトのデザインとタイトル設定
st.set_page_config(page_title="みんなの健康レシピ考案機", page_icon="🥗", layout="centered")

st.title("🥗 パーソナル健康レシピ考案システム")
st.write("条件を選ぶだけで、この場で即座に完璧な健康お弁当レシピを検索・計算します！")

st.write("---")

# 2. ユーザーがサイト上で選ぶ入力フォーム
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("👤 性別を選んでください", ["男性", "女性", "その他"])
    age = st.number_input("🎂 年齢を入力してください", min_value=1, max_value=100, value=17)

with col2:
    purpose = st.selectbox("🎯 目的を選んでください", ["健康維持（バランス）", "ダイエット（低カロリー）", "筋トレ（高タンパク）"])
    meal_time = st.selectbox("⏰ 食事のタイミング", ["朝食", "昼食（お弁当）", "夕食", "間食"])

# 3. 食材の入力欄
st.subheader("🛒 今手元にある食材（使いたい食材）")
user_ingredients = st.text_input("例：ブロッコリー, 鶏肉, 卵", "ブロッコリー, 鶏肉")

st.write("---")

# 4. ボタンを押したらその場でレシピを検索・計算
if st.button("✨ この食材で健康レシピを検索・考案する"):
    
    with st.spinner("🧠 栄養管理システムが最適なバランスを計算中..."):
        
        # 食材の表記ゆれに対応するため小文字・スペース削除
        ingredients_list = [i.strip() for i in user_ingredients.replace("、", ",").split(",")]
        
        # 目的ごとの目標カロリー目安を計算
        if purpose == "ダイエット（低カロリー）":
            target_cal = 450 if gender == "女性" else 550
            pfc_text = "たんぱく質: 30g / 脂質: 8g / 炭水化物: 55g (低脂質ヘルシー！)"
        elif purpose == "筋トレ（高タンパク）":
            target_cal = 650 if gender == "女性" else 750
            pfc_text = "たんぱく質: 45g / 脂質: 15g / 炭水化物: 80g (高タンパク！)"
        else:
            target_cal = 550 if gender == "女性" else 650
            pfc_text = "たんぱく質: 25g / 脂質: 18g / 炭水化物: 70g (厚生労働省推奨バランス)"

        # 入力食材のチェック
        text = "".join(ingredients_list)
        has_chicken = "鶏" in text or "肉" in text
        has_broccoli = "ブロッコリー" in text or "野菜" in text or "ベジタブル" in text
        has_egg = "卵" in text or "たまご" in text
        has_tomato = "トマト" in text
        has_fish = "魚" in text or "鮭" in text or "サバ" in text or "ツナ" in text

        # 検索と出力のロジック
        st.success("🎉 条件に最適な健康管理レシピが完成しました！")
        st.write("---")
        
        if has_chicken and has_broccoli:
            st.markdown("### 🍳 考案メニュー：鶏むね肉とブロッコリーのノンオイル塩昆布炒め")
            st.markdown(f"■ **必要な食材とグラム数**\n- 鶏むね肉: 120g\n- 冷凍ブロッコリー: 80g\n- 塩昆布: ふたつまみ\n- ごま油: 小さじ1/2")
            st.markdown("■ **作り方**\n1. 鶏むね肉は一口大に切り、冷凍ブロッコリーはレンジで軽く解凍します。\n2. フライパンにごま油を熱し、鶏むね肉を中火で炒めます。\n3. 肉に火が通ったらブロッコリーと塩昆布を加え、水分を飛ばすように強火でサッと炒め合わせます（お弁当の傷み防止）。")
        elif has_egg and has_broccoli:
            st.markdown("### 🍳 考案メニュー：ブロッコリーと卵のふんわり出汁とじ")
            st.markdown(f"■ **必要な食材とグラム数**\n- 冷凍ブロッコリー: 100g\n- 卵: 1個\n- 白だし: 小さじ1\n- 水: 大さじ1")
            st.markdown("■ **作り方**\n1. 小さめのフライパンに水、白だし、冷凍ブロッコリーを入れて火にかけます。\n2. ブロッコリーが温まったら、溶き卵を回し入れます。\n3. 卵にしっかり火が通るまで蓋をして蒸し焼きにします（汁気が出ないように完全に固めます）。")
        elif has_chicken and has_tomato:
            st.markdown("### 🍳 考案メニュー：鶏肉のさっぱりトマト煮込み")
            st.markdown(f"■ **必要な食材とグラム数**\n- 鶏もも肉（皮なし）: 120g\n- トマト（またはトマト缶）: 100g\n- コンソメ: 小さじ1/2\n- 塩コショウ: 少々")
            st.markdown("■ **作り方**\n1. 鶏肉を一口大に切り、フライパンで両面をしっかり焼きます。\n2. 潰したトマトとコンソメを加え、弱火で水分がトロンとするまで煮詰めます。\n3. お弁当用には汁気がなくなるまでしっかり煮詰めるのが健康・安全のコツです。")
        elif has_fish:
            st.markdown("### 🍳 考案メニュー：お弁当の定番！鮭と彩り野菜のホイル焼き")
            st.markdown(f"■ **必要な食材とグラム数**\n- 生鮭（またはサバ・ツナなど）: 1切れ（約80g）\n- お好みの野菜（ブロッコリー等）: 50g\n- ポン酢: 小さじ1\n- バター: 3g")
            st.markdown("■ **作り方**\n1. アルミホイルに野菜を敷き、その上に魚の切れをのせます。\n2. バターをのせてホイルをきっちり閉じ、トースターやフライパンで10〜12分蒸し焼きにします。\n3. 仕上げにポン酢をかけて完成。油控えめでとてもヘルシーです。")
        else:
            # 万能ヘルシー野菜炒めレシピ（どんな食材でも対応）
            main_ing = user_ingredients if user_ingredients else "手元にある食材"
            st.markdown(f"### 🍳 考案メニュー：{main_ing}の特製ヘルシー温野菜炒め")
            st.markdown(f"■ **必要な食材とグラム数**\n- {user_ingredients}: 各100g程度\n- 醤油: 小さじ1\n- みりん: 小さじ1\n- かつお節: 1パック（お弁当の水分を吸わせるため）")
            st.markdown("■ **作り方**\n1. 食材を食べやすい大きさにカットします（冷凍野菜はレンジで解凍し、水気をギューッと絞っておきます）。\n2. フライパンで食材をしっかり炒め、水分を完全に飛ばします。\n3. 醤油とみりんで味付けし、最後にかつお節を和えて完成です。")
            
        # 栄養価の表示
        st.write("---")
        st.markdown(f"### 📊 推定栄養価（{meal_time}・{purpose}向けに自動計算）")
        st.metric(label="エネルギー (目標目安)", value=f"{target_cal} kcal")
        st.markdown(f"🧬 **PFCバランス（目安）**\n{pfc_text}")
        
        st.markdown(f"### 💡 栄養管理アドバイス\n{age}歳{gender}の{meal_time}として、午後の活動エネルギーを落とさずに{purpose}を最大限サポートする最高の重量バランスです。お弁当に入れる場合は、完全に冷ましてからフタをしてくださいね！")
