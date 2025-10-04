---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a Ph.D. student in the [Translational AI Research Lab](https://tair-lab.github.io/) at <b>King’s College London (KCL)</b>, advised by [Dr. Yunpeng Li](https://yunpengli.ac/) and [Prof. Yulan He](https://sites.google.com/view/yulanhe). My research focuses on multimodal artificial intelligence for dental diagnosis, with the goal of advancing healthcare applications through cutting-edge machine learning methods.

Before joining KCL, I worked as a Research Assistant at the <b>Institute for AI Industry Research (AIR), Tsinghua University</b>, where I collaborated closely with [Prof. Zaiqing Nie](https://air.tsinghua.edu.cn/en/info/1046/1192.htm) and [Dr. Haibao Yu](https://scholar.google.com/citations?user=JW4F5HoAAAAJ) on research related to autonomous driving perception, planning and simulation. I obtained my Master’s degree from the <b>Department of Automation, Tsinghua University</b>, supervised by [Prof. Biqing Huang](https://www.au.tsinghua.edu.cn/en/info/1092/3354.htm). My master’s research primarily focused on computer vision for industrial defect inspection. I received my Bachelor degree (with Hons.) from <b>Shenyuan Honors College, Beihang University</b>.

I have published several papers in high-level AI conferences and journals, with total <a href='https://scholar.google.com/citations?user=msJSbWYAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https://raw.githubusercontent.com/ryhnhao/ryhnhao.github.io/google-scholar-stats/gs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> citations on Google Scholar.

My current research interests lie in multimodal learning, computer vision, and medical AI, with a special focus on their applications in dentistry and healthcare.

<!-- # 🔥 News

- _2022.02_: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
- _2022.02_: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

# 📝 Publications

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">arXiv 2025</div> <img src='images/styledrive.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[StyleDrive: Towards Driving-Style Aware Benchmarking of End-To-End Autonomous Driving](https://arxiv.org/pdf/2506.23982)

<b>Ruiyang Hao</b>, Bowen Jing, Haibao Yu, Zaiqing Nie

arXiv: 2506.23982, <i>Under Review</i>. [**_Project_**](https://styledrive.github.io/), [**_Ref_**](https://ry-hao.top/files/styledrive.txt)

- Novel large-scale real-world personalized driving dataset
- High-quality multi-stage annotation pipeline
- First standardized benchmark for personalized E2EAD
- Significant gains in human-like behavior via personalization
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">arXiv 2025</div> <img src='images/DriveE2E.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[DriveE2E: Closed-Loop Benchmark for End-to-End Autonomous Driving through Real-to-Simulation](https://arxiv.org/pdf/2509.23922)

Haibao Yu<sup>\*</sup>, Wenxian Yang<sup>\*</sup>, <b>Ruiyang Hao<sup>\*</sup></b>, Chuanye Wang<sup>\*</sup>, Jiaru Zhong<sup>\*</sup>, Ping Luo, Zaiqing Nie (\* means equal contributions)

arXiv: 2509.23922, <i>Under Review</i>. [**_Project_**](https://github.com/AIR-THU/DriveE2E), [**_Ref_**](https://ry-hao.top/files/drivee2e.txt)

- Infra-view-enhanced real2sim framework for realistic closed-loop evaluation.
- 15 high-fidelity digital twins & 800 infra-sensor diverse scenarios.
- Comprehensive closed-loop benchmark with expert dataset for SOTA evaluation and IL training.
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">CVPR 2024</div> <img src='images/RCooper.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[RCooper: A Real-world Large-scale Dataset for Roadside Cooperative Perception](https://openaccess.thecvf.com/content/CVPR2024/papers/Hao_RCooper_A_Real-world_Large-scale_Dataset_for_Roadside_Cooperative_Perception_CVPR_2024_paper.pdf)

<b>Ruiyang Hao</b>, Siqi Fan, Yingru Dai, Zhenlin Zhang, Chenxi Li, Yuntian Wang, Haibao Yu, Wenxian Yang, Jirui Yuan, Zaiqing Nie

<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)</i>, 22347-22357. [**_Project_**](https://github.com/AIR-THU/DAIR-RCooper), [**_Ref_**](https://ry-hao.top/files/CVPR24.txt)

- 1st real-world large-scale dataset for roadside cooperative perception.
- 50k images & 30k point clouds with 3D annotations across 10 semantic classes.
- Benchmarks on 3D detection & tracking with SOTA results, proving effectiveness of cooperation.
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">AEI 2022</div> <img src='images/AEI2022.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Efficient surface defect detection using self-supervised learning strategy and segmentation network](https://www.sciencedirect.com/science/article/pii/S1474034622000386)

Ronge Xu<sup>\*</sup>, <b>Ruiyang Hao<sup>\*</sup></b>, Biqing Huang (\* means equal contributions)

<i>Advanced Engineering Informatics</i>, 2022, 52: 101566. [**_Ref_**](https://ry-hao.top/files/AEI22.txt)

- Lightweight defect detection for efficient and accurate industrial inspection.
- Attention & multi-task strategy to enhance defect focus and edge segmentation.
- Self-supervised learning with homographic enhancement and synthetic datasets to reduce annotation cost and improve generalization.
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">JIM 2021</div> <img src='images/JIM2021.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[A steel surface defect inspection approach towards smart industrial monitoring](https://link.springer.com/article/10.1007/s10845-020-01670-2)

<b>Ruiyang Hao</b>, Bingyu Lu, Ying Cheng, Xiu Li, Biqing Huang

<i>Journal of Intelligent Manufacturing</i>, 2021, 32(7): 1833-1843. [**_Ref_**](https://ry-hao.top/files/JIM21.txt)

- DIN: steel defect inspection network balancing efficiency and performance.
- Deformable convolution backbone for adaptive feature extraction on diverse defect shapes.
- Balanced feature pyramid fusion for accurate multi-size defect inspection.
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">CAIE 2021</div> <img src='images/CAIE2021.jpg' alt="sym" width="80%" style="display:block; margin:0 auto;"></div></div>
<div class='paper-box-text' markdown="1">
[Manufacturing service supply-demand optimization with dual diversities for industrial internet platforms](https://www.sciencedirect.com/science/article/pii/S0360835221001418)

<b>Ruiyang Hao</b>, Ying Cheng, Yongping Zhang, Fei Tao

<i>Computers & Industrial Engineering</i>, 2021, 156: 107237. [**_Ref_**](https://ry-hao.top/files/CAIE21.txt)

- Classified hypernetwork & MS-SDR for modeling dual diversities in supply-demand.
- MS-SDO model with stakeholder analysis to enhance platform stability and utility.
- Knowledge-guided NSGAII + experiments for effective optimization and management insights.
</div>
</div>

- [Research Challenges and Progress in the End-to-End V2X Cooperative Autonomous Driving Competition](https://arxiv.org/pdf/2507.21610), <b>Ruiyang Hao</b>, Haibao Yu, Jiaru Zhong, Chuanye Wang, Jiahao Wang, Yiming Kan, et al. <i>International Conference on Computer Vision Workshop (ICCVW 2025)</i>, 2025. [**_Ref_**](https://ry-hao.top/files/ICCVW25.txt)

- [A Domain Incremental Learning Framework for PCB Continuous Defect Detection](https://ieeexplore.ieee.org/abstract/document/10922142), Ze Yan, <b>Ruiyang Hao</b>, Biqing Huang, Lin Zhu, Hui Pan. <i>IEEE Transactions on Instrumentation and Measurement</i>, 2025, 74: 5016613. [**_Ref_**](https://ry-hao.top/files/TIM25.txt)

- [Incremental Template Neighborhood Matching for 3D anomaly detection](https://www.sciencedirect.com/science/article/pii/S0925231224002546), Jiaxun Wang, Xiang Wang, <b>Ruiyang Hao</b>, Haonan Yin, Biqing Huang, Xiao Xu, Jingxian Liu. <i>Neurocomputing</i>, 2024, 74: 5016613. [**_Ref_**](https://ry-hao.top/files/NEURC24.txt)

- [Metal surface defect detection method based on improved cascade r-cnn](https://asmedigitalcollection.asme.org/computingengineering/article-abstract/24/4/041002/1169612/Metal-Surface-Defect-Detection-Method-Based-on), Yani Wang, Xiang Wang, <b>Ruiyang Hao</b>, Bingyu Lu, Biqing Huang. <i>Journal of Computing and Information Science in Engineering</i>, 2024, 24(4): 041002. [**_Ref_**](https://ry-hao.top/files/JCISE24.txt)

# 🎖 Honors and Awards

- _2025.10_ <b>Newland Pedley Studentship</b>, awarded by King's College London.
- _2018.12_ <b>National Scholarship</b>, the Top Scholarship in China, <b>top 1%</b>.
- _2022.10_ First-class Excellence Scholarship, awarded by Tsinghua University, <b>top 2.5%</b>.
- _2021.10_ First-class Excellence Scholarship, awarded by Tsinghua University, <b>top 2.5%</b>.
- _2020.10_ Outstanding graduate & the honored degree, awarded by Beihang University, <b>top 5%</b>.
- _2019.4_ Meritorious Prize of Interdisciplinary Contest in Modeling, awarded by COMAP, <b>top 8%</b> of contestants.
- _2018.4_ Meritorious Prize of Interdisciplinary Contest in Modeling, awarded by COMAP, <b>top 8%</b> of contestants.

# 📖 Educations

- _2025.10 - now_, PhD, <b>King's College London</b>, London, UK.
- _2020.09 - 2023.06_, Master, with <b>4.00/4.00 GPA (ranking 1/155)</b>, <b>Tsinghua University</b>, Beijing, China.
- _2016.09 - 2020.06_, Bachelor (w. Honor), with <b>3.83/4.00 GPA (ranking 1/51)</b>, <b>Beihang University</b>, Beijing, China.

# 💻 Internships and RAs

- _2025.07 - 2025.10_, Tuojing Intelligence, Internship: _Simulation and Generation in Autonomous Driving_.
- _2023.07 - 2025.07_, Tsinghua University, Research Assistant: _Perception, Planning and Simulation in Autonomous Driving_.
- _2022.06 - 2022.10_, SenseTime Research, Internship: _Perception in Unmanned Aerial Vehicle_.

# 💬 Services

- _Since 2024_, Conference Reviewer of _ECCV_, _ICLR_, _NIPS_, _AAAI_, _CVPR_, etc.
- _Since 2023_, Journal Reviewer of _Advanced Engineering Informatics_, _Journal of Industrial Information Integration_, _Journal of Real-Time Image Processing_, _The Visual Computer_, _Signal, Image and Video Processing_, etc.
- _2025.06_, Area Chair, CVPR 2025 Workshop on Multi-Agent Embodied Intelligent System.
- _2024.10_, Program Committee Member, ECCV 2024 Workshop on Coop-Intelligence.
