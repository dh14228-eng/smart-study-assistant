"""
Internationalization (i18n) translations for Smart Study Assistant.
Supports English (en) and Arabic (ar).
"""

TRANSLATIONS = {
    "English": {
        "page_title": "Smart Study Assistant",
        "app_title": "Smart Study Assistant",
        "app_caption": "Your AI study companion for understanding difficult topics, summarizing notes, and testing your knowledge.",
        "sidebar_title": "🎓 Study Assistant",
        "sidebar_caption": "AI-powered Academic & Study Helper",
        "language_label": "🌐 Language / اللغة",
        "nav_label": "Navigation",
        "nav_qa": "❓ Academic Q&A",
        "nav_summary": "📝 Summarize Notes",
        "nav_explain": "💡 Explain Difficult Concepts",
        "nav_quiz": "🎯 Quiz & Question Generator",
        "settings_header": "Settings & API Key",
        "api_key_active": "API Key active ({provider}).",
        "api_key_label": "API Key (OpenAI or OpenRouter)",
        "api_key_placeholder": "sk-...",
        "api_key_help": "Your API key is kept securely in your local browser session.",
        "api_key_stored": "API key stored in session!",
        "api_key_missing_info": "Add your API key in .env or above to enable live AI responses.",
        "model_label": "AI Model",
        "model_help": "gpt-4o-mini is recommended for fast, cost-effective study assistance.",
        "version_info": "Version 1.1.0 • Bilingual Edition",

        # Feature 1: QA
        "qa_header": "Academic Question Answering",
        "qa_desc": "Ask any academic question and receive a structured, student-friendly explanation.",
        "qa_subject_label": "Subject / Field",
        "qa_subjects": ["General", "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "History", "Literature", "Economics", "Other"],
        "qa_depth_label": "Explanation Style",
        "qa_depths": ["Standard (Clear & Direct)", "Concise (Quick Summary)", "In-Depth (Step-by-step with formulas/examples)"],
        "qa_input_label": "Enter your question:",
        "qa_input_placeholder": "e.g., How does photosynthesis work? or Explain the difference between stack and heap memory.",
        "qa_button": "Get Answer",
        "qa_result_title": "Answer",
        "qa_field_name": "Question",

        # Feature 2: Summary
        "summary_header": "Study Content Summarizer",
        "summary_desc": "Paste your lecture notes, textbook chapters, or articles to get concise summaries.",
        "summary_format_label": "Summary Format",
        "summary_formats": [
            "Key Bullet Points & Takeaways",
            "Structured Executive Summary",
            "Flashcard / Q&A Format",
            "Quick TL;DR (1 Paragraph)"
        ],
        "summary_length_label": "Summary Length",
        "summary_lengths": ["Ultra-Short", "Medium", "Comprehensive"],
        "summary_input_label": "Paste your study content or notes below:",
        "summary_input_placeholder": "Paste notes, lecture transcripts, or textbook excerpts here...",
        "summary_button": "Summarize Content",
        "summary_result_title": "Summary",
        "summary_field_name": "Study Notes",

        # Feature 3: Explain
        "explain_header": "Simple Concept Explainer",
        "explain_desc": "Break down complicated topics into simple, intuitive mental models and real-world analogies.",
        "explain_concept_label": "Concept or Topic Name:",
        "explain_concept_placeholder": "e.g., Quantum Entanglement, Recursion, Inflation, Mitosis",
        "explain_audience_label": "Explanation Level",
        "explain_audiences": [
            "Like I'm 5 (Simple & Fun Analogy)",
            "High School Student (Clear & Intuitive)",
            "College Student (Balanced Depth & Clarity)",
            "Real-World Analogy Focused"
        ],
        "explain_context_label": "Additional Context or specific questions about the concept (optional):",
        "explain_context_placeholder": "e.g., I don't understand the base case in recursion, or explain how it connects to everyday life.",
        "explain_button": "Simplify Concept",
        "explain_result_title": "Simplified Explanation",
        "explain_field_name": "Concept Name",

        # Feature 4: Quiz
        "quiz_header": "AI Study Quiz & Question Generator",
        "quiz_desc": "Generate practice questions from topics or study notes to test your understanding.",
        "quiz_type_label": "Question Type",
        "quiz_types": [
            "Multiple Choice (MCQ)",
            "True / False with Explanations",
            "Short Answer & Discussion Questions",
            "Mixed Format"
        ],
        "quiz_num_label": "Number of Questions",
        "quiz_diff_label": "Difficulty Level",
        "quiz_diffs": ["Easy / Beginner", "Intermediate", "Advanced / Exam Level"],
        "quiz_input_label": "Enter Topic or Paste Notes to generate questions from:",
        "quiz_input_placeholder": "e.g., Newton's Laws of Motion, or paste a summary of European History...",
        "quiz_button": "Generate Quiz Questions",
        "quiz_result_title": "Practice Questions",
        "quiz_field_name": "Quiz Topic/Notes",

        # Warnings & Errors
        "warn_empty": "Please enter text for {field_name}.",
        "warn_too_long": "{field_name} is too long ({count} characters). Maximum allowed is {max_chars} characters.",
        "err_api_missing": "API Key Missing: Please set your OPENAI_API_KEY in a .env file or enter it securely in the sidebar to generate AI responses.",
        "err_auth_failed": "Authentication Failed: Invalid API Key for {provider}. Please verify your key in the sidebar or .env file.",
        "err_rate_limit": "Rate Limit Exceeded: API rate limit reached. Please wait a moment and try again.",
        "err_quota": "Quota Exceeded: Your {provider} account has exceeded its current quota or credit balance.",
        "err_generic": "Error generating response: {msg}",
        "footer_text": "Smart Study Assistant • Developed following PRD, AGENTS.md, and SECURITY_RULES.md guidelines."
    },
    "العربية": {
        "page_title": "المساعد الدراسي الذكي",
        "app_title": "المساعد الدراسي الذكي",
        "app_caption": "رفيقك الدراسي المدعوم بالذكاء الاصطناعي لفهم المفاهيم الصعبة وتلخيص الملاحظات وتوليد أسئلة الاختبارات.",
        "sidebar_title": "🎓 المساعد الدراسي",
        "sidebar_caption": "مساعد أكاديمي ودراسي ذكي",
        "language_label": "🌐 Language / اللغة",
        "nav_label": "الأقسام والخدمات",
        "nav_qa": "❓ إجابة الأسئلة الأكاديمية",
        "nav_summary": "📝 تلخيص المحتوى والملاحظات",
        "nav_explain": "💡 تبسيط المفاهيم الصعبة",
        "nav_quiz": "🎯 توليد الاختبارات والأسئلة",
        "settings_header": "الإعدادات ومفتاح API",
        "api_key_active": "مفتاح API نشط ومفعل ({provider}).",
        "api_key_label": "مفتاح API (OpenAI أو OpenRouter)",
        "api_key_placeholder": "sk-...",
        "api_key_help": "يتم حفظ المفتاح بأمان داخل جلستك المحلية فقط دون مشاركته.",
        "api_key_stored": "تم حفظ مفتاح API في الجلسة بنجاح!",
        "api_key_missing_info": "أضف مفتاح API في ملف .env أو في الحقل أعلاه لتفعيل استجابات الذكاء الاصطناعي.",
        "model_label": "نموذج الذكاء الاصطناعي",
        "model_help": "يوصى بنموذج gpt-4o-mini لسرعته العالية ودقته وتكلفته الاقتصادية.",
        "version_info": "الإصدار 1.1.0 • النسخة ثنائية اللغة",

        # Feature 1: QA
        "qa_header": "إجابة الأسئلة الأكاديمية",
        "qa_desc": "اطرح أي سؤال دراسي أو أكاديمي واحصل على شرح منظم ومبسط وواضح.",
        "qa_subject_label": "المادة / التخصص",
        "qa_subjects": ["عام", "الرياضيات", "الفيزياء", "الكيمياء", "الأحياء", "علوم الحاسب", "التاريخ", "الأدب واللغات", "الاقتصاد", "أخرى"],
        "qa_depth_label": "أسلوب الشرح",
        "qa_depths": ["قياسي (شرح واضح ومباشر)", "موجز (مختصر وسريع)", "متعمق (خطوة بخطوة مع القوانين والأمثلة)"],
        "qa_input_label": "اكتب سؤالك الأكاديمي هنا:",
        "qa_input_placeholder": "مثال: كيف تحدث عملية البناء الضوئي؟ أو اشرح الفرق بين الذاكرة Stack و Heap في البرمجة.",
        "qa_button": "الحصول على الإجابة",
        "qa_result_title": "الإجابة والشرح",
        "qa_field_name": "السؤال",

        # Feature 2: Summary
        "summary_header": "تلخيص المحتوى والملاحظات الدراسية",
        "summary_desc": "الصق ملاحظات المحاضرات أو فصول الكتب أو المقالات للحصول على ملخصات دقيقة ومفيدة.",
        "summary_format_label": "صيغة التلخيص",
        "summary_formats": [
            "نقاط رئيسية وأهم الاستنتاجات",
            "ملخص تنفيذي منظم ومترابط",
            "صيغة بطاقات دراسية (سؤال وجواب)",
            "ملخص سريع وموجز (فقرة واحدة)"
        ],
        "summary_length_label": "حجم الملخص",
        "summary_lengths": ["قصير جداً", "متوسط", "شامل ومفصل"],
        "summary_input_label": "الصق المحتوى أو الملاحظات الدراسية أدناه:",
        "summary_input_placeholder": "الصق نصوص المحاضرات أو الملخصات هنا...",
        "summary_button": "بدء التلخيص",
        "summary_result_title": "الملخص الدراسي",
        "summary_field_name": "الملاحظات الدراسية",

        # Feature 3: Explain
        "explain_header": "تبسيط وشرح المفاهيم المعقدة",
        "explain_desc": "تبسيط الموضوعات الصعبة باستخدام التشبيهات الواقعية والأمثلة العملية والنماذج الذهنية السلسة.",
        "explain_concept_label": "اسم المفهوم أو الموضوع:",
        "explain_concept_placeholder": "مثال: التشابك الكمي، الاستدعاء الذاتي (Recursion)، التضخم الاقتصادي، الانقسام الميتوزي",
        "explain_audience_label": "مستوى الشرح المستهدف",
        "explain_audiences": [
            "اشرح كأنني في الخامسة من عمري (تشبيهات بسيطة وممتعة)",
            "طالب مرحلة ثانوية (واضح وبديهي)",
            "طالب جامعي (متوازن بين العمق والوضوح)",
            "التركيز على التشبيهات والأمثلة الواقعية"
        ],
        "explain_context_label": "سياق إضافي أو جانب محدد ترغب بالتركيز عليه (اختياري):",
        "explain_context_placeholder": "مثال: أواجه صعوبة في فهم شرط التوقف (Base Case)، أو وضح علاقته بالحياة اليومية.",
        "explain_button": "تبسيط المفهوم",
        "explain_result_title": "الشرح المبسط",
        "explain_field_name": "اسم المفهوم",

        # Feature 4: Quiz
        "quiz_header": "توليد الأسئلة والاختبارات الدراسية",
        "quiz_desc": "توليد أسئلة تدريبية واختبارات قصيرة من الموضوعات أو الملاحظات لاختبار مدى استيعابك وفهمك.",
        "quiz_type_label": "نوع الأسئلة",
        "quiz_types": [
            "اختيار من متعدد (MCQ)",
            "صح أو خطأ مع التعليل",
            "أسئلة إجابات قصيرة ونقاشية",
            "نموذج اختبار متنوع"
        ],
        "quiz_num_label": "عدد الأسئلة",
        "quiz_diff_label": "مستوى الصعوبة",
        "quiz_diffs": ["سهل / مبتدئ", "متوسط", "متقدم / مستوى امتحانات"],
        "quiz_input_label": "اكتب الموضوع أو الصق الملاحظات لتوليد الأسئلة منها:",
        "quiz_input_placeholder": "مثال: قوانين نيوتن للحركة، أو الصق ملخصاً عن تاريخ الحضارة الإسلامية...",
        "quiz_button": "توليد الأسئلة التدريبية",
        "quiz_result_title": "الأسئلة التدريبية والإجابات النموذجية",
        "quiz_field_name": "موضوع الاختبار/الملاحظات",

        # Warnings & Errors
        "warn_empty": "يرجى إدخال نص في حقل {field_name}.",
        "warn_too_long": "النص المدخل في {field_name} طويل جداً ({count} حرف). الحد الأقصى المسموح به هو {max_chars} حرف.",
        "err_api_missing": "مفتاح API غير متوفر: يرجى ضبط OPENAI_API_KEY في ملف .env أو إدخاله بأمان في الشريط الجانبي لتوليد الإجابات.",
        "err_auth_failed": "فشل المصادقة: مفتاح API غير صالح لمزود الخدمة {provider}. يرجى التحقق من المفتاح في الشريط الجانبي أو ملف .env.",
        "err_rate_limit": "تم تجاوز حد الطلبات: يرجى الانتظار للحظات ثم إعادة المحاولة.",
        "err_quota": "تم تجاوز الحصة: لقد استنفد حسابك لدى {provider} الرصيد أو الحصة المتاحة.",
        "err_generic": "حدث خطأ أثناء توليد الاستجابة: {msg}",
        "footer_text": "المساعد الدراسي الذكي • تم التطوير وفقاً لمتطلبات PRD وإرشادات الأمان AGENTS.md و SECURITY_RULES.md."
    }
}
