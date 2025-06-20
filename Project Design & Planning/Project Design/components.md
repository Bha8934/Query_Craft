## 🧩 COMPONENT-WISE FLOWCHARTS & EXPLANATIONS

---

### ✅ 1. **Streamlit Page Setup**

#### **Flowchart**

```
[Start app.py]
   ↓
[Set page config with title, icon, layout]
   ↓
[Set main title: "Welcome to QueryCraft!"]
```

#### **Explanation**

* The app starts by initializing the **page layout** using `st.set_page_config()`.
* It defines the browser **tab title**, **emoji icon**, and layout (`wide`).
* The main welcome message is set with `st.title()`.

> This is your visual and structural setup — happens once when the app loads.

---

### ✅ 2. **Two-Column Layout (Streamlit Columns)**

#### **Flowchart**

```
[Divide page into col1 (3) and col2 (2)]
   ↓
[Display markdown in col1]
   ↓
[Display image in col2]
```

#### **Explanation**

* `col1` shows the **introductory text** with `st.markdown()` which explains what QueryCraft is and its use cases.
* `col2` tries to **load an image** (`icon.png`) from the `images/` directory. If not found, it loads a placeholder image from a URL.

> This two-column layout keeps UI engaging and responsive.

---

### ✅ 3. **Image Handling Component**

#### **Flowchart**

```
[Try to open local image "images/icon.png"]
   ↓
    [Found] → Display with st.image()
   ↓
    [Not Found] → Load fallback placeholder image
```

#### **Explanation**

* A `try/except` block is used for fault tolerance. If the app can't find the image, it doesn't crash—it shows a placeholder.
* `Image.open()` loads local images, and `st.image()` renders them.

> This ensures a professional UI even if the asset is missing.

---

### ✅ 4. **Welcome Text Block (Markdown)**

#### **Flowchart**

```
[st.markdown()]
   ↓
[Render multi-line introductory text]
```

#### **Explanation**

* This section uses rich Markdown formatting to explain:

  * What QueryCraft does
  * Who it's for
  * Why it's useful
* This text improves **user onboarding** and **first impressions**.

> It’s your elevator pitch — shown right when users land on the app.

---

### ✅ 5. **Sidebar Navigation (Hint Message)**

#### **Flowchart**

```
[st.success("Use the sidebar to get started.")]
   ↓
[User notices sidebar for navigation]
```

#### **Explanation**

* A success message guides users to use the **Streamlit sidebar** to explore further.
* This is **not a widget**, but a gentle visual cue to drive interaction.

---

## 🗂 COMPONENT SUMMARY TABLE

| Component                      | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| `st.set_page_config()`         | Initializes app appearance in the browser      |
| `st.title()`                   | Sets main heading of the page                  |
| `st.columns()`                 | Splits screen for layout and responsive design |
| `st.markdown()`                | Displays rich text description                 |
| `st.image()`                   | Shows logo or placeholder image                |
| `try/except FileNotFoundError` | Handles missing image file gracefully          |
| `st.success()`                 | Adds visual cue for sidebar navigation         |

---

## ✅ Optional Combined Master Flow (Welcome Page Logic)

```
[App Starts] 
   ↓
[Set page title and layout]
   ↓
[Create columns (col1, col2)]
   ↓                    ↓
[Render intro text]    [Try loading image]
                             ↓
                 [Load success] OR [Load fallback]
   ↓
[Display horizontal rule (---)]
   ↓
[Show success message: "Use sidebar"]
```

---

