<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/header-dark.svg">
  <img src="../assets/header-light.svg" width="542" alt="freiversum – Linux, open source and tech you run yourself">
</picture>

Open source apps for the Linux desktop and Android, written and maintained by Christoph Langner ([@linuxundich](https://github.com/linuxundich)). Small tools that do one job well, built with the platform's own toolkit.

[Website](https://freiversum.de/en/) &nbsp;·&nbsp; [Blog](https://linuxundich.de/en/) &nbsp;·&nbsp; [Mastodon](https://social.anoxinon.de/@linuxundich) &nbsp;·&nbsp; [All repositories](https://github.com/orgs/freiversum/repositories)

<table>
  <tr>
    <td width="25%" valign="top"><b>Native</b><br><sub>GTK 4 and libadwaita on GNOME, Kirigami on Plasma, Jetpack Compose on Android</sub></td>
    <td width="25%" valign="top"><b>Local first</b><br><sub>Works on your network and your machine, no account where none is needed</sub></td>
    <td width="25%" valign="top"><b>No tracking</b><br><sub>No analytics and no ads in the apps</sub></td>
    <td width="25%" valign="top"><b>Free software</b><br><sub>Open licenses, mostly GPL-3.0, English and German, developed in the open</sub></td>
  </tr>
</table>

## Linux desktop

<table>
  <tr>
    <td width="33%" align="center" valign="top"><a href="https://github.com/freiversum/gnomos"><img src="../assets/shots/gnomos.webp" alt="Gnomos showing an album grid"></a><br><sub>Gnomos</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://github.com/freiversum/ScreenForge"><img src="../assets/shots/screenforge.webp" alt="ScreenForge main window"></a><br><sub>ScreenForge</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://github.com/freiversum/tretlager"><img src="../assets/shots/tretlager.webp" alt="Tretlager during a ride"></a><br><sub>Tretlager</sub></td>
  </tr>
</table>

| | Project | What it does | Get it |
|---|---|---|---|
| <img src="../assets/icons/gnomos.png" width="32" alt=""> | [**Gnomos**](https://github.com/freiversum/gnomos)<br><sub>C++ · GTK 4</sub> | Sonos controller, local network only | [Flatpak, .deb](https://github.com/freiversum/gnomos/releases/latest) |
| <img src="../assets/icons/parkett.png" width="32" alt=""> | [**Parkett**](https://github.com/freiversum/parkett)<br><sub>Rust · GTK 4</sub> | Terminal with splits, the Tilix way | [Source](https://github.com/freiversum/parkett/releases/latest) |
| <img src="../assets/icons/dandelion.png" width="32" alt=""> | [**Dandelion**](https://github.com/freiversum/dandelion)<br><sub>Python · GTK 4</sub> | Post to Mastodon, Bluesky and more at once | [Flatpak](https://github.com/freiversum/dandelion/releases/latest) |
| <img src="../assets/icons/screenforge.png" width="32" alt=""> | [**ScreenForge**](https://github.com/freiversum/ScreenForge)<br><sub>Rust · GTK 4</sub> | Compose smartphone screenshots | [Build from source](https://github.com/freiversum/ScreenForge#readme) |
| <img src="../assets/icons/tretlager.png" width="32" alt=""> | [**Tretlager**](https://github.com/freiversum/tretlager)<br><sub>Python · Kirigami</sub> | Zwift on Linux, with a Bluetooth sensor bridge | [Flatpak, .deb](https://github.com/freiversum/tretlager/releases/latest) |
| <img src="../assets/icons/pulsgeber.png" width="32" alt=""> | [**Pulsgeber**](https://github.com/freiversum/pulsgeber)<br><sub>GNOME Shell</sub> | TUXEDO Control Center profiles in Quick Settings | [Extension ZIP](https://github.com/freiversum/pulsgeber/releases/latest) |

## Android

<table>
  <tr>
    <td width="33%" align="center" valign="top"><a href="https://github.com/freiversum/planetfoss-android"><img src="../assets/shots/planetfoss-android.webp" width="150" alt="PlanetFOSS radar tab"></a><br><sub>PlanetFOSS</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://github.com/freiversum/hausmusik"><img src="../assets/shots/hausmusik.webp" width="150" alt="Hausmusik now playing"></a><br><sub>Hausmusik</sub></td>
    <td width="33%" align="center" valign="top"><a href="https://github.com/freiversum/commentator"><img src="../assets/shots/commentator.webp" width="150" alt="Commentator comment inbox"></a><br><sub>Commentator</sub></td>
  </tr>
</table>

| | Project | What it does | Get it |
|---|---|---|---|
| <img src="../assets/icons/planetfoss-android.png" width="32" alt=""> | [**PlanetFOSS**](https://github.com/freiversum/planetfoss-android)<br><sub>Kotlin · Compose</sub> | Linux and open source news reader | [APK](https://github.com/freiversum/planetfoss-android/releases/latest) · [Google Play (test)](https://play.google.com/apps/testing/net.planetfoss.app) |
| <img src="../assets/icons/hausmusik.png" width="32" alt=""> | [**Hausmusik**](https://github.com/freiversum/hausmusik)<br><sub>Kotlin · Compose</sub> | Local Sonos controller, also for S1 players | [APK](https://github.com/freiversum/hausmusik/releases/latest) |
| <img src="../assets/icons/commentator.png" width="32" alt=""> | [**Commentator**](https://github.com/freiversum/commentator)<br><sub>Kotlin · WordPress plugin</sub> | Moderate WordPress comments from your phone | [APK](https://github.com/freiversum/commentator/releases/latest) |

<details>
<summary><b>Libraries and building blocks</b></summary>
<br>

[**prospekt**](https://github.com/freiversum/prospekt) – procedural backgrounds that look designed. The Rust/Cairo generator behind ScreenForge, usable on its own.

</details>

## Contributing

> [!TIP]
> Bug reports, ideas and pull requests go straight to the project's repository. Translations are welcome; most apps ship in English and German.

Before larger changes, please open an issue first so we can talk about the approach. Security issues: use *Report a vulnerability* in the repository instead of a public issue.

<br>
<p align="center">
  <a href="https://freiversum.de/en/"><img src="../assets/mark.svg" width="20" alt=""></a><br>
  <sub>A star in the <a href="https://freiversum.de/en/">freiversum</a></sub>
</p>
