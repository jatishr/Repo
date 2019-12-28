def workSpace;
node
{
    stage("Checkout")
    {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '2f70483c-7858-4087-ada6-6a5cdfae89dd', url: 'https://github.com/jatishr/Repo']]])
        workSpace=pwd()
    }
    stage("Static code Ananlysis")
    {
        echo"Static code Ananlysis"
    }
    stage("Build")
    {
        echo"Build now"
    }
}