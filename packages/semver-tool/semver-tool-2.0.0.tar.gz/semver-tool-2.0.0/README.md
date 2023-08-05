## semver-tool

Print SemVer version for a git project. Git tags must match `v?M.N.P` pattern.
You can print specific version components using fotmat string.

Full format string is MNPRBD, where:
 * M - major
 * N - minor
 * P - patch
 * R - prerelease
 * B - build
 * D - dirty


## Usage

Examples:
```
$ semver-tool
4.1.2-rc2+gb10c717
$ semver-tool -f MNPR
4.1.2-rc2
$ semver-tool -f MNPR --rc dev
4.1.2-dev2
```

## Use Cases
### Build docker images
I use this tool to build docker images using SemVer schema.
The flow is this:
 * build `image:latest` with `Commit` label
 * push it as `image:M.N.P-R`
 * push it as `image:M.N.P`
 * push it as `image:M.N`

My build script has this code
```bash
current=$(semver_tool -f MNPR)
docker build --label Commit=$(semver_tool) -t image:$current
docker tag image:$current image $(semver_tool -f MNP)
docker tag image:$current image $(semver_tool -f MN)
```
which results in these images
```
image   1.2.3-rc2
image   1.2.3
image   1.2
```
Each image has `Commit` label with semver description, eg, `1.2.3-rc2+g22eeff`
