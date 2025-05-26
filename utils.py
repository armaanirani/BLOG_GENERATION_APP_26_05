import os
from dotenv import load_dotenv


from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = "llama-3.3-70b-versatile"
llm = ChatGroq(
    model=model,
    temperature=0,
    api_key=GROQ_API_KEY
)

def generate_blog(blog_topic, blog_wordcount, blog_style, blog_tone, blog_audience):
    template1 = """
    You're an experienced writer with a skill for creating highly engaging blog posts that capture the attention of your audience and deliver value. 
    Write a {blog_wordcount} word minimum blog post on the topic '{blog_topic}' in a {blog_style} style and {blog_tone} tone.
    The post should be tailored for {blog_audience} and should include relevant examples, insights, and actionable takeaways.
    Ensure the content is well-structured, informative, and engaging, with a clear introduction, body, and conclusion.
    Use subheading, bullet points, and other formatting techniques to enhance readability and engagement.
    Include relevant keywords and phrases to optimize the blog post for search engines, while maintaining a natural flow of language.
    The blog post should be original, well-researched, and free of plagiarism.
    Please provide a compelling and informative blog post that meets these criteria.
    """
    
    template2 = """
    **Blog Generation Framework**
    Create a comprehensive blog post that strictly adheres to these parameters:

    1. **Core Requirements**
    - Topic: {blog_topic}
    - Word Count: {blog_wordcount} (±5%)
    - Style: {blog_style} (Match associated vocabulary and structure)
    - Tone: {blog_tone} (Maintain consistently throughout)
    - Audience: {blog_audience} (Tailor complexity and examples)

    2. **Structural Guidelines**
    a) Introduction (15% of content):
    - Hook with surprising statistic/quote/question
    - Clear thesis statement
    - Roadmap of content

    b) Body (70% of content) - Organize into 3-5 sections with:
    - H2/H3 headers using power words
    - Data-driven arguments (include 2-3 statistics per section)
    - Real-world examples from authoritative sources
    - Bullet points for lists (>3 items)
    - Callout boxes for key insights

    c) Conclusion (15% of content):
    - Restate key takeaways
    - Actionable next steps
    - Provocative closing thought

    3. **Style Execution**
    - {blog_style} Style Requirements:
        {{
        Professional: Industry jargon OK, third-person perspective
        Casual: Contractions allowed, conversational phrasing
        Technical: Include code snippets/equations where relevant
        Storytelling: Character/narrative arc, sensory details
        }}[match selected style]

    4. **Tone Implementation**
    - Primary Tone: {blog_tone}
    - Tone Guide:
        {{
        Authoritative: Industry expert voice, confident assertions
        Friendly: Inclusive language ("we"/"you"), em-dash asides
        Humorous: Witty analogies, pop culture references
        Inspirational: Success stories, motivational language
        }}[match selected tone]

    5. **SEO & Readability**
    - Primary Keyword: [topic-derived]
    - Secondary Keywords: 3-5 semantically related terms
    - Keyword density: 1-1.5% (natural integration)
    - Flesch Reading Ease: >60 (adjust sentence length)
    - Use transition words between paragraphs

    6. **Quality Assurance**
    - Zero plagiarism: Unique perspectives only
    - Fact-check all claims (include sources where needed)
    - Avoid passive voice (>90% active voice)
    - Limit adverbs (<2% of total words)
    - Vary sentence structure (10-25 words avg.)

    **Output Formatting**
    Return in clean markdown with:
    - # Title
    - ## Section Headers
    - ### Subheaders
    - **Bold** key terms
    - Bullet/numbered lists
    - > Blockquotes for citations
    --- Section separators
    """
    
    template3 = """
    {{#system}}
    You are a professional, SEO-savvy content writer adept at creating in-depth, engaging, and well-structured blog posts.
    Always ensure accuracy, cite sources when appropriate, and avoid hallucinations.
    {{/system}}

    {{#user}}
    Topic: **{blog_topic}**  
    Target Word Count: **at least {blog_wordcount} words**  
    Writing Style: **{blog_style}**  
    Tone: **{blog_tone}**  
    Audience: **{blog_audience}**

    Please produce:
    1. **A brief SEO meta description** (1-2 sentences).  
    2. **A clear title** and **subtitle**.  
    3. **Table of Contents** with clickable section names.  
    4. **Blog post** with:
        - Hook-style introduction.  
        - Multiple well-titled sections/subheadings.  
        - Use of bullet points, numbered lists, or call-out boxes for key takeaways.  
        - At least two concrete examples or case studies.  
        - Actionable insights or “next steps” at the end of each main section.  
        - Smooth logical flow and transitions.  
    5. **Conclusion** summarizing key points and including a clear call-to-action (CTA).  
    6. **Optional further reading/resources** (links or citations).

    **Formatting & SEO**:
    - Include relevant keywords naturally throughout.  
    - Use Markdown formatting (## for headings, **bold**, _italics_, etc.).  
    - Ensure all headings are H2 or deeper (i.e., “##”, “###”).  
    - Provide alt-text suggestions for any images you mention.

    **Quality checks** (self-review before output):
    - Verify factual accuracy.  
    - Keep paragraphs ≤ 4 sentences.  
    - Avoid jargon; explain any necessary technical terms.  
    - Run a final “read-aloud” check for flow and engagement.

    Now, write the blog post.  
    {{/user}}
    """
    
    template = """
    **Task:** Write a high-quality blog post based on the following parameters.

    **Parameters:**
    - **Topic:** {blog_topic}
    - **Word Count:** {blog_wordcount} words (minimum; target length may vary)
    - **Style:** {blog_style} (e.g., formal, casual, conversational, technical, storytelling)
    - **Tone:** {blog_tone} (e.g., authoritative, friendly, encouraging, analytical)
    - **Audience:** {blog_audience} (e.g., professionals, students, beginners, parents)

    **Instructions:**
    1. **Structure:**
        - **Introduction:** Hook the reader with a question, statistic, or anecdote.
        - **Body:** Break into 3–5 subheadings. Use bullet points, lists, or examples to clarify complex ideas.
        - **Conclusion:** Summarize key takeaways and encourage engagement (e.g., comments, sharing).

    2. **Content Requirements:**
        - Include **actionable insights** (e.g., "Try this 3-step process").
        - Add **real-world examples** or case studies relevant to {blog_audience}.
        - Provide **data or research** (e.g., "According to a 2023 study...").
        - Use **keywords naturally** (e.g., {blog_topic}, {blog_audience} needs, {blog_style} approach).

    3. **Tone & Style:**
        - Match the {blog_tone} and {blog_style} throughout the post.
        - Avoid jargon unless targeting a technical audience.
        - Use a conversational tone if the audience is casual (e.g., parents, students).

    4. **SEO Optimization:**
        - Include 2-3 primary keywords (e.g., {blog_topic}, {blog_audience} tips, {blog_style} guide).
        - Add a meta description (e.g., "Learn how to [blog_topic] for {blog_audience} with this {blog_style} guide").

    5. **Originality & Quality:**
        - Ensure content is **original**, well-researched, and free of plagiarism.
        - Avoid generic advice; focus on **unique value** for {blog_audience}.

    **Output:**
    Provide the blog post in a **natural, human-like tone**. Format it with subheadings, bullet points, and clear paragraphs. Avoid markdown formatting unless explicitly requested.
    """
    prompt = PromptTemplate(
        input_variables=["blog_topic", "blog_wordcount", "blog_style", "blog_tone", "blog_audience"],
        template=template1
    )
    
    response = llm(prompt.format(
        blog_topic=blog_topic,
        blog_wordcount=blog_wordcount,
        blog_style=blog_style,
        blog_tone=blog_tone,
        blog_audience=blog_audience
    ))
    
    print(response)
    
    return response