# [GoatStyles][GS] by [GoatBytes.IO][GB]`() {`

## Introduction

:wave: Welcome to GoatStyles, a repository for professional code style guides, where we strive to
uphold the highest standards of software engineering.

In the realm of code style guides, we understand that opinions vary, and decisions often balance
between necessity and subjectivity. However, amidst this diversity of perspectives, one principle
remains paramount: __consistency__. By adhering to a consistent style, developers can enhance
readability, maintainability, and collaboration within their codebases.

## Styles

Click on the programming language logo to view the style guide for that language.

|                    ▁▁▁▁▁▁▁                     |                              ▁▁▁▁▁▁▁                               |                    ▁▁▁▁▁▁▁                     |                ▁▁▁▁▁▁▁                 |                  ▁▁▁▁▁▁▁                   |                            ▁▁▁▁▁▁▁                             |
|:----------------------------------------------:|:------------------------------------------------------------------:|:----------------------------------------------:|:--------------------------------------:|:------------------------------------------:|:--------------------------------------------------------------:|
|       [![C++][CPP_Logo]][CPP]<br>**C**++       |               [![C#][CSharp_Logo]][CSharp]<br>**C**#               |     [![Dart][Dart_Logo]][Dart]<br>**Dart**     |     [![Go][Go_Logo]][Go]<br>**Go**     |   [![Java][Java_Logo]][Java]<br>**Java**   | [![JavaScript][JavaScript_Logo]][JavaScript]<br>**JavaScript** |
| [![Kotlin][Kotlin_Logo]][Kotlin]<br>**Kotlin** | [![Objective-C][Objective-C_Logo]][Objective-C]<br>**Objective-C** | [![Python][Python_Logo]][Python]<br>**Python** | [![Rust][Rust_Logo]][Rust]<br>**Rust** | [![Swift][Swift_Logo]][Swift]<br>**Swift** | [![TypeScript][TypeScript_Logo]][TypeScript]<br>**TypeScript** |

## Badges

Enhance your project's documentation by adding our style guide badges, signaling to fellow
developers the coding standards and conventions your project adheres to. Each badge links directly
to a comprehensive style guide for its respective programming language.

[![Style Guide-C++](https://img.shields.io/badge/Style%20Guide-C++-00599C.svg?style=flat&labelColor=black&color=00599C&logo=cplusplus)](https://styles.goatbytes.io/lang/cpp)
[![Style Guide-C#](https://img.shields.io/badge/Style%20Guide-C%23-178600.svg?style=flat&labelColor=black&color=178600&logo=csharp)](https://styles.goatbytes.io/lang/csharp)
[![Style Guide-Dart](https://img.shields.io/badge/Style%20Guide-Dart-00B4AB.svg?style=flat&labelColor=black&color=00B4AB&logo=dart)](https://styles.goatbytes.io/lang/dart)
[![Style Guide-Go](https://img.shields.io/badge/Style%20Guide-Go-00ADD8.svg?style=flat&labelColor=black&color=00ADD8&logo=go)](https://styles.goatbytes.io/lang/go)
[![Style Guide-Java](https://img.shields.io/badge/Style%20Guide-Java-ED8B00.svg?style=flat&labelColor=black&color=ED8B00&logo=java)](https://styles.goatbytes.io/lang/java)
[![Style Guide-JavaScript](https://img.shields.io/badge/Style%20Guide-JavaScript-F0DB4F.svg?style=flat&labelColor=black&color=F0DB4F&logo=javascript)](https://styles.goatbytes.io/lang/javascript)
[![Style Guide-Kotlin](https://img.shields.io/badge/Style%20Guide-Kotlin-7F52FF.svg?style=flat&labelColor=black&color=7F52FF&logo=kotlin)](https://styles.goatbytes.io/lang/kotlin)
[![Style Guide-Objective-C](https://img.shields.io/badge/Style%20Guide-Objective--C-438EFF.svg?style=flat&labelColor=black&color=438EFF)](https://styles.goatbytes.io/lang/objective-c)
[![Style Guide-Python](https://img.shields.io/badge/Style%20Guide-Python-3776AB.svg?style=flat&labelColor=black&color=3776AB&logo=python)](https://styles.goatbytes.io/lang/python)
[![Style Guide-Rust](https://img.shields.io/badge/Style%20Guide-Rust-DEA584.svg?style=flat&labelColor=black&color=DEA584&logo=rust)](https://styles.goatbytes.io/lang/rust)
[![Style Guide-Shell](https://img.shields.io/badge/Style%20Guide-Shell-4EAA25.svg?style=flat&labelColor=black&color=4EAA25&logo=gnu-bash)](https://styles.goatbytes.io/lang/shell)
[![Style Guide-Swift](https://img.shields.io/badge/Style%20Guide-Swift-FA7343.svg?style=flat&labelColor=black&color=FA7343&logo=swift)](https://styles.goatbytes.io/lang/swift)
[![Style Guide-TypeScript](https://img.shields.io/badge/Style%20Guide-TypeScript-3178C6.svg?style=flat&labelColor=black&color=3178C6&logo=typescript)](https://styles.goatbytes.io/lang/typescript)

## Project Overview

### Programming Languages

GoatStyles provides comprehensive style guides for C++, C#, Dart, Go, Java, JavaScript, Kotlin,
Objective-C, Python, Rust, Shell, Swift, and TypeScript. Our aim is to support a wide range of
development environments, catering to the diverse needs of the software development community.

### Technology Stack and Tools

- **MKDocs** for a fast and user-friendly static site generation.
- **GitHub Actions** and **GitHub Pages** for automated deployments and hosting.
- **JavaScript**, **CSS**, and **Markdown**

### Repository Structure

The GoatStyles style guides are meticulously documented in Markdown and located within the
[`docs/lang`](docs/lang) directory of the repository.

## How to Contribute

We encourage contributions to GoatStyles! Before making a contribution, please review our
[contributing](docs/contributing.md) guidelines. All contributors must complete our
[Individual Contributor License Agreement (CLA)][CLA] before their code can be accepted.

Forking the repository and proposing changes through pull requests are great ways to contribute.
Though not all suggestions may be accepted, your contributions are highly appreciated and crucial
to the project's growth and diversity.

## Build Instructions

To build and serve the GoatStyles site locally, follow these instructions:

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your machine. You can check your
  Python version by running `python --version` in your terminal.
- **Git**: Make sure Git is installed for cloning the repository.

### Steps

1. **Clone the Repository**
    - Use Git to clone the GoatStyles repository to your local machine:
      ```shell
      git clone https://github.com/goatbytes/GoatStyles.git
      cd GoatStyles
      ```

2. **Set Up Python Environment (Optional)**
    - It's recommended to create a virtual environment to keep dependencies required by the project
      separate from your global Python environment:
      ```shell
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```

3. **Install Dependencies**
    - Install the required Python packages including MkDocs and its extensions used by the project:
      ```shell
      pip install mkdocs mkdocs-material pymdown-extensions mkdocs-minify-plugin neoteroi-mkdocs mkdocs-git-revision-date-localized-plugin
      ```

4. **Build the MkDocs Site**
    - Build the static site files with MkDocs:
      ```shell
      mkdocs build
      ```
    - This command generates the site static files in the `site` directory.

5. **Serve the Site Locally**
    - To preview the site on your local machine, run:
      ```shell
      mkdocs serve
      ```
    - This command starts a local web server that serves the GoatStyles site. You can view the site
      by navigating to `http://127.0.0.1:8000` in your web browser.

6. **Making Changes**
    - You can now make changes to the Markdown files. The site will automatically rebuild and
      refresh the browser page when you save changes.

## About GoatBytes.IO

![GoatBytesLogo](https://storage.googleapis.com/ktor-goatbytes.appspot.com/images/logo/1000h/goatbytes-logo-with-text.png)

At **GoatBytes.IO**, our mission is to develop secure software solutions that empower businesses to
transform the world. With a focus on innovation and excellence, we strive to deliver cutting-edge
products that meet the evolving needs of businesses across various industries.

[![GitHub](https://img.shields.io/badge/GitHub-GoatBytes-181717?logo=github)](https://github.com/goatbytes)
[![Twitter](https://img.shields.io/badge/Twitter-GoatBytes-1DA1F2?logo=twitter)](https://twitter.com/goatbytes)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GoatBytes-0077B5?logo=linkedin)](https://www.linkedin.com/company/goatbytes)
[![Instagram](https://img.shields.io/badge/Instagram-GoatBytes.io-E4405F?logo=instagram)](https://www.instagram.com/goatbytes.io/)

## License

[GoatStyles][GH] is licensed under [Attribution-ShareAlike 4.0 International][LICENSE]

# `};`

[//]: # (@formatter:off)

[GS]: https://styles.goatbytes.io
[GB]: https://goatbytes.io
[GH]: https://github.com/goatbytes/GoatStyles
[LICENSE]: https://creativecommons.org/licenses/by-sa/4.0/
[CLA]: https://forms.gle/J5iqyH4hrHQQDfUCA

<!-- Logo URLs -->
[CPP_Logo]: ./docs/assets/img/cplusplus.svg
[CSharp_Logo]: ./docs/assets/img/csharp.svg
[Dart_Logo]: ./docs/assets/img/dart.svg
[Go_Logo]: ./docs/assets/img/go.svg
[Java_Logo]: ./docs/assets/img/java.svg
[JavaScript_Logo]: ./docs/assets/img/javascript.svg
[Kotlin_Logo]: ./docs/assets/img/kotlin.svg
[Objective-C_Logo]: ./docs/assets/img/objective-c.svg
[Python_Logo]: ./docs/assets/img/python.svg
[Rust_Logo]: ./docs/assets/img/rust.svg
[Swift_Logo]: ./docs/assets/img/swift.svg
[TypeScript_Logo]: ./docs/assets/img/typescript.svg

<!-- Page URLs -->
[CPP]: https://styles.goatbytes.io/lang/cpp/
[CSharp]: https://styles.goatbytes.io/lang/csharp/
[Dart]: https://styles.goatbytes.io/lang/dart/
[Go]: https://styles.goatbytes.io/lang/go/
[Java]: https://styles.goatbytes.io/lang/java/
[JavaScript]: https://styles.goatbytes.io/lang/javascript/
[Kotlin]: https://styles.goatbytes.io/lang/kotlin/
[Objective-C]: https://styles.goatbytes.io/lang/objc/
[Python]: https://styles.goatbytes.io/lang/python/
[Rust]: https://styles.goatbytes.io/lang/rust/
[Swift]: https://styles.goatbytes.io/lang/swift/
[TypeScript]: https://styles.goatbytes.io/lang/typescript/
