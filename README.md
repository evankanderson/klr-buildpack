# Python Knative Lambda Runtime builder

This repo contains the source code for a builder (buildpacks + `builder.toml`) for converting AWS Lambda functions written for Python3 into HTTP-compatible containers for use with Knative or OpenFaaS.

This work is largely derived from https://github.com/triggermesh/aws-custom-runtime and https://github.com/triggermesh/knative-lambda-runtime, but with packaging which is friendly to https://github.com/knative-sandbox/kn-plugin-func

# Using with `kn func`

There is a pre-built copy of this builder at `docker.io/ekanderson/klr-builder:0.0.4`. These directions assume you want to use that builder, rather than building your own (see below for build-your-own instructions). Note that you may need a `kn func` **with https://github.com/knative-sandbox/kn-plugin-func/pull/591**.

Once you have the templates in the local func repositories, you can run the following commands to get started:

```shell
kn func create a-demo -l aws-python -r https://github.com/evankanderson/klr-buildpack
```

This will create a directory called `a-demo` which contains your function code. You can `cd` into it and then run:

```
kn func deploy
```

To deploy to the cluster selected by your kubernetes configuration.

# Development / rebuilding

Most of the actual content is in `buildpack/bin`; these are the copied components of the TriggerMesh `aws-custom-runtime` (pre-built) and `knative-lambda-runtime` (copied/vendored).

Once you have versions of those you are happy with, you can publish them to a repo like dockerhub with:

```shell
(cd buildpack && pack buildpack package ekanderson/klr-addin:0.1.0 --publish) && (cd metabuild && pack buildpack package ekanderson/klr-buildpack:0.0.4 --config package.toml --publish) && pack builder create ekanderson/klr-builder:0.0.4 --config ./builder.toml --publish
```

(Unless you have access to the `ekanderson` account, you'll need to switch that string for your own. You may also need to switch that in all the `*.toml` files in this repo as well.)

You can also try using the `pack` CLI to test the buildpack without the rest of the `func` infrastructure, which can be handy sometimes.