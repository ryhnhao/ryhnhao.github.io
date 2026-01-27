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

I am currently a Ph.D. student in the [Translational AI Research Lab](https://tair-lab.github.io/) at <b>King’s College London (KCL)</b>, advised by [Dr. Yunpeng Li](https://yunpengli.ac/) and [Prof. Yulan He](https://sites.google.com/view/yulanhe).

Before joining KCL, I was a Research Assistant at the <b>Institute for AI Industry Research (AIR), Tsinghua University</b>, where I worked with [Prof. Zaiqing Nie](https://air.tsinghua.edu.cn/en/info/1046/1192.htm) and [Dr. Haibao Yu](https://scholar.google.com/citations?user=JW4F5HoAAAAJ) on autonomous driving perception, planning, and simulation. I obtained my Master’s degree from the <b>Department of Automation, Tsinghua University</b> under the supervision of [Prof. Biqing Huang](https://www.au.tsinghua.edu.cn/en/info/1092/3354.htm), focusing on computer vision for industrial defect inspection. I received my Bachelor’s degree (with Honours) from <b>Shenyuan Honors College, Beihang University</b>. These experiences built a strong foundation in multimodal perception and machine learning systems, which now support my current research on medical AI for dental diagnosis.

I have published multiple papers in leading AI conferences and journals, with total <a href='https://scholar.google.com/citations?user=msJSbWYAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https://raw.githubusercontent.com/ryhnhao/ryhnhao.github.io/google-scholar-stats/gs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> citations on Google Scholar.

<b>Research Focus</b>: Multimodal learning, computer vision, and medical AI, with a particular emphasis on dental and healthcare applications.

<div style="margin-top: 25px; margin-bottom: 0; text-align: center;">
  <img src="https://ry-hao.top/images/images.png" 
       style="width: 100%; max-width: 1200px; height: auto; border-radius: 8px;">
</div>

<p style="text-align: center; font-size: 14px; color: #444; margin-top: 4px; font-weight: 500;">
  Advancing Dental Diagnosis through Multimodal AI!
</p>

<!-- # 🔥 News

- _2022.02_: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.
- _2022.02_: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

# 📝 Publications

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">AAAI 2026 (Oral)</div> <img src='images/styledrive.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[StyleDrive: Towards Driving-Style Aware Benchmarking of End-to-End Autonomous Driving](https://arxiv.org/pdf/2506.23982)

<b>Ruiyang Hao</b>, Bowen Jing, Haibao Yu, Zaiqing Nie

<i>The 40th Annual AAAI Conference on Artificial Intelligence (AAAI 2026)</i>. [**_Project_**](https://styledrive.github.io/), [**_Video_**](https://youtu.be/M3_zA0CT-Zg), [**_Ref_**](https://ry-hao.top/files/styledrive.txt), [![Stars](https://img.shields.io/github/stars/AIR-THU/StyleDrive?style=flat&logo=github)](https://github.com/AIR-THU/StyleDrive)

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

arXiv: 2509.23922, <i>Under Review</i>. [**_Project_**](https://github.com/AIR-THU/DriveE2E), [**_Ref_**](https://ry-hao.top/files/drivee2e.txt), [![Stars](https://img.shields.io/github/stars/AIR-THU/DriveE2E?style=flat&logo=github)](https://github.com/AIR-THU/DriveE2E)

- Infra-view-enhanced real2sim framework for realistic closed-loop evaluation.
- 15 high-fidelity digital twins & 800 infra-sensor diverse scenarios.
- Comprehensive closed-loop benchmark with expert dataset for SOTA evaluation and IL training.
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">ICCVW 2025</div> <img src='images/UniV2X_challenge.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Research Challenges and Progress in the End-to-End V2X Cooperative Autonomous Driving Competition](https://openaccess.thecvf.com/content/ICCV2025W/DriveX/papers/Hao_Research_Challenges_and_Progress_in_the_End-to-End_V2X_Cooperative_Autonomous_ICCVW_2025_paper.pdf)

<b>Ruiyang Hao</b>, Haibao Yu, Jiaru Zhong, Chuanye Wang, Jiahao Wang, Yiming Kan, Wenxian Yang, Siqi Fan, Huilin Yin, Jianing Qiu, Yao Mu, Jiankai Sun, Li Chen, Walter Zimmer, Dandan Zhang, Shanghang Zhang, Mac Schwager, Ping Luo, Zaiqing Nie

<i>International Conference on Computer Vision Workshop (ICCVW 2025)</i>, 2025, 1828–1839. [**_Project_**](https://github.com/AIR-THU/UniV2X), [**_Video_**](https://youtu.be/LS0CrJ9jfEs), [**_Ref_**](https://ry-hao.top/files/ICCVW25.txt), [![Stars](https://img.shields.io/github/stars/AIR-THU/UniV2X?style=flat&logo=github)](https://github.com/AIR-THU/UniV2X)

- First V2X challenge combining sequential perception & E2E planning.
- Demonstrated SOTA advances in V2X cooperative perception & E2E planning.
- Key insights on V2X fusion, robust planning, & future V2X system design.
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">CVPR 2024</div> <img src='images/RCooper.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[RCooper: A Real-world Large-scale Dataset for Roadside Cooperative Perception](https://openaccess.thecvf.com/content/CVPR2024/papers/Hao_RCooper_A_Real-world_Large-scale_Dataset_for_Roadside_Cooperative_Perception_CVPR_2024_paper.pdf)

<b>Ruiyang Hao</b>, Siqi Fan, Yingru Dai, Zhenlin Zhang, Chenxi Li, Yuntian Wang, Haibao Yu, Wenxian Yang, Jirui Yuan, Zaiqing Nie

<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)</i>, 2024, 22347-22357. [**_Project_**](https://github.com/AIR-THU/DAIR-RCooper), [**_Video_**](https://youtu.be/6CFi9Bz4wg4), [**_Ref_**](https://ry-hao.top/files/CVPR24.txt), [![Stars](https://img.shields.io/github/stars/AIR-THU/DAIR-RCooper?style=flat&logo=github)](https://github.com/AIR-THU/DAIR-RCooper)

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

- Classified hypernetwork & MS-SDR to model diversities in supply-demand.
- MS-SDO optimization to enhance platform stability and utility.
- Knowledge-guided NSGAII algorithm for effective optimization, providing insights for platform management.
</div>
</div>

- [A Domain Incremental Learning Framework for PCB Continuous Defect Detection](https://ieeexplore.ieee.org/abstract/document/10922142), Ze Yan, <b>Ruiyang Hao</b>, Biqing Huang, Lin Zhu, Hui Pan. <i>IEEE Transactions on Instrumentation and Measurement</i>, 2025, 74: 5016613. [**_Ref_**](https://ry-hao.top/files/TIM25.txt)

- [Incremental Template Neighborhood Matching for 3D anomaly detection](https://www.sciencedirect.com/science/article/pii/S0925231224002546), Jiaxun Wang, Xiang Wang, <b>Ruiyang Hao</b>, Haonan Yin, Biqing Huang, Xiao Xu, Jingxian Liu. <i>Neurocomputing</i>, 2024, 581: 127483. [**_Ref_**](https://ry-hao.top/files/NEURC24.txt)

- [Metal surface defect detection method based on improved cascade r-cnn](https://asmedigitalcollection.asme.org/computingengineering/article-abstract/24/4/041002/1169612/Metal-Surface-Defect-Detection-Method-Based-on), Yani Wang, Xiang Wang, <b>Ruiyang Hao</b>, Bingyu Lu, Biqing Huang. <i>Journal of Computing and Information Science in Engineering</i>, 2024, 24(4): 041002. [**_Ref_**](https://ry-hao.top/files/JCISE24.txt)

# 🎖 Honors and Awards

- _Oct 2025–Sep 2028_, <b>Newland Pedley Studentship</b>, King's College London.
- _Oct 2025_, <b>Research Excellence Scholarship</b>, University College London (declined due to enrollment constraints), <b>top 40 Worldwide</b>.
- _Dec 2018_, <b>National Scholarship</b>, the Top Scholarship in China, <b>top 1%</b>.
- _Oct 2022_, First-class Excellence Scholarship, Tsinghua University, <b>top 2.5%</b>.
- _Oct 2021_, First-class Excellence Scholarship, Tsinghua University, <b>top 2.5%</b>.
- _Jun 2020_, Outstanding Graduate with Honours, Beihang University, <b>top 5%</b>.
- _Apr 2019_, Meritorious Prize of Interdisciplinary Contest in Modeling, COMAP, <b>top 8%</b>.
- _Apr 2018_, Meritorious Prize of Interdisciplinary Contest in Modeling, COMAP, <b>top 8%</b>.

# 📖 Education

- _Oct 2025–now_, PhD, <b>King's College London</b>, London, UK.
- _Sep 2020–Jun 2023_, Master, with <b>4.00/4.00 GPA (Rank: 1/155)</b>, <b>Tsinghua University</b>, Beijing, China.
- _Sep 2016–Jun 2020_, Bachelor (with Honours), with <b>3.83/4.00 GPA (Rank: 1/51)</b>, <b>Beihang University</b>, Beijing, China.

# 💻 Internships and RAs

- _Jul 2025–Oct 2025_, Tuojing Intelligence, Internship: _Simulation and Generation in Autonomous Driving_.
- _Jul 2023–Jul 2025_, Tsinghua University, Research Assistant: _Perception, Planning and Simulation in Autonomous Driving_.
- _Jun 2022–Oct 2022_, SenseTime Research, Internship: _Perception in Unmanned Aerial Vehicle_.

# 💼 Services

- _Since 2024_, <b>Conference Reviewer</b> for _CVPR_, _NeurIPS_, _AAAI_, _ECCV_, _ICLR_, etc.
- _Since 2023_, <b>Journal Reviewer</b> for _Advanced Engineering Informatics_, _Journal of Industrial Information Integration_, _Journal of Real-Time Image Processing_, _The Visual Computer_, _Signal, Image and Video Processing_, etc.
- _Jun 2025_, <b>Area Chair</b>, CVPR 2025 Workshop on Multi-Agent Embodied Intelligent Systems.
- _Oct 2024_, <b>Program Committee Member</b>, ECCV 2024 Workshop on Coop-Intelligence.

# 💬 Talks and Oral Presentations

- _Jan 2026_, <b>StyleDrive: Towards Personalized End-to-end Autonomous Driving</b>, Annual AAAI Conference on Artificial Intelligence, Singapore.
- _Dec 2025_, <b>Tooth Bone Loss Estimation Based on 3D CBCT Data</b>, Bellairs Workshop on Machine Learning and Statistical Signal Processing for Data on Graphs, Saint James Parish, Barbados.
- _Nov 2025_, <b>Real2Sim in Autonomous Driving Systems</b>, Invited Internal Talk, Department of Civil, Environmental and Geomatic Engineering, University College London, London, UK.
- _Oct 2025_, <b>End-to-End V2X Cooperative Autonomous Driving Challenges</b>, ICCV Workshop on Foundation Models for V2X-Based Cooperative Autonomous Driving, Honolulu, Hawaii, USA.
