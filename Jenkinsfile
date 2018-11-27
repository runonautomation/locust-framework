
node {
    properties([
        parameters([
            string(name: 'LOCUST_HOST', defaultValue: 'https://google.com'),
            string(name: 'SCENARIO', defaultValue: 'locustfiles/helloworld.yaml'),
            string(name: 'OUT_DIR', defaultValue: 'out'),
            string(name: 'REPORT', defaultValue: 'simulation.xml'),
        ])
    ])
    stage("Checkout source code"){
        checkout scm
    }
    stage("Run tests"){
        def testImage = docker.build("locust-training:${env.BUILD_ID}")
        testImage.inside {
            def bztSettings = "-o settings.artifacts-dir=${env.OUT_DIR} -o scenarios.productpage.default-address=${params.LOCUST_HOST}"
            sh "bzt ${bztSettings} ${env.SCENARIO} -report"
            sh "ls -lahr ${env.OUT_DIR}"
            perfReport "${env.OUT_DIR}/${env.REPORT}"
            archiveArtifacts artifacts: "${env.OUT_DIR}/**/*"
        }
    } 
}
