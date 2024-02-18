## Inspiration
Our journey to creating this project stems from a shared realization: the path from idea to execution is fraught with inefficiencies that can dilute even the most brilliant concepts. As developers with a knack for turning visions into reality, we've faced the slow erosion of enthusiasm and value that time imposes on innovation. This challenge is magnified for those outside the technical realm, where a lack of coding skills transforms potential breakthroughs into missed opportunities. Harvard Business Review and TechCrunch analyzed Y Combinator startups and found that around 40% of founders are non-technical.

Drawing from our experiences in fast-paced sectors like health and finance, we recognized the critical need for speed and agility. The ability to iterate quickly and gather user feedback is not just beneficial but essential in these fields. Yet, this process remains a daunting barrier for many, including non-technical visionaries whose ideas have the potential to reshape industries.

With this in mind, we set out to democratize the development process. Our goal was to forge a tool that transcends technical barriers, enabling anyone to bring their ideas to life swiftly and efficiently. By leveraging our skills and insights into the needs of both developers and non-developers alike, we've crafted a solution that bridges the gap between imagination and tangible innovation, ensuring that no idea is left unexplored due to the constraints of technical execution.

This project is more than just a tool; it's a testament to our belief that the right technology can unlock the potential within every creative thought, transforming fleeting ideas into impactful realities.

## What it does
Building on the foundation laid by your vision, MockupMagic represents a leap toward democratizing digital innovation. By transforming sketches into interactive prototypes, we not only streamline the development process but also foster a culture of inclusivity where ideas, not technical prowess, stand in the spotlight. This tool is a catalyst for creativity, enabling individuals from diverse backgrounds to participate actively in the digital creation sphere.

The user can upload a messy sketch on paper to our website. MockupMagic will then digitize your low-fidelity prototype into a high-fidelity replica with interactive capabilities. The user can also see code alongside the generated mockups, which serves as both a bridge to tweak the generated prototype and a learning tool, gently guiding users toward deeper technical understanding. Moreover, the integration of a community feedback mechanism through the Discussion tab directly within the platform enhances the iterative design process, allowing for real-time user critique and collaboration.

MockupMagic is more than a tool; it's a movement towards a future where the digital divide is narrowed, and the translation of ideas into digital formats is accessible to all. By empowering users to rapidly prototype and refine their concepts, we're not just accelerating the pace of innovation; we're ensuring that every great idea has the chance to be seen, refined, and realized in the digital world. 

## How we built it
Conceptualization: The project began with brainstorming sessions where we discussed the challenges non-technical individuals face in bringing their ideas to life. Understanding the value of quick prototyping, especially for designers and founders with creative but potentially fleeting ideas, we focused on developing a solution that accelerates this process.

Research and Design: We conducted research to understand the needs of our target users, including designers, founders, and anyone in between who might lack technical skills. This phase helped us design a user-friendly interface that would make it intuitive for users to upload sketches and receive functional web mockups.

Technology Selection: Choosing the right technologies was crucial. We decided on a combination of advanced image processing and AI algorithms capable of interpreting hand-drawn sketches and translating them into HTML, CSS, and JavaScript code. We leveraged and finetuned existing AI models from MonsterAPI and GPT API and tailored them to our specific needs for better accuracy in digitizing sketches.

Development: The development phase involved coding the backend logic that processes the uploaded sketches, the AI model integration for sketch interpretation, and the frontend development for a seamless user experience. We used the Reflex platform to build out our user-facing website, capitalizing on their intuitive Python-like web development tools.

Testing and Feedback: Rigorous testing was conducted to ensure the accuracy of the mockups generated from sketches. We also sought feedback from early users, including designers and founders, to understand how well the tool met their needs and what improvements could be made.

## Challenges we ran into
We initially began by building off our own model, hoping to aggregate quality training data mapping hand-drawn UI components to final front-end components, but we quickly realized this data was very difficult to find and hard to scrape for. Our model performs well for a few screens however it still struggles to establish connections between multiple screens or more complex actions.

## Accomplishments that we're proud of
Neither of us had much front-end & back-end experience going into this hackathon, so we made it a goal to use a framework that would give us experience in this field. After learning about Reflex during our initial talks with sponsors, we were amazed that Web Apps could be built in pure Python and wanted to jump right in. Using Reflex was an eye-opening experience because we were not held back by preconceived notions of traditional web development - we got to enjoy learning about Reflex and how to build products with it. Reflex’s novelty also translates to limited knowledge about it within LLM tools developers use to help them while coding, this helped us solidify our programming skills through reading documentation and creative debugging methodologies - skills almost being abstracted away by LLM coding tools. Finally, our favorite part about doing hackathons is building products we enjoy using. It helps us stay aligned with the end user while giving us personal incentives to build the best hack we can. 

## What we learned
Through this project, we learned that we aren’t afraid to tackle big problems in a short amount of time. Bringing ideas on napkins to full-fledged projects is difficult, and it became apparent hitting all of our end goals would be difficult to finish in one weekend. We quickly realigned and ensured that our MVP was as good as it could get before demo day.

## What's next for MockupMagic
We would like to fine-tune our model to handle more edge cases in handwritten UIs. While MockupMagic can handle a wide range of scenarios, we hope to perform extensive user testing to figure out where we can improve our model the most. Furthermore, we want to add an easy deployment pipeline to give non-technical founders even more autonomy without knowing how to code. As we continue to develop MockupMagic, we would love to see the platform being used even at TreeHacks next year by students who want to rapidly prototype to test several ideas!
