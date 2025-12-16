exports.config ={
port:3000,
avnapp_host : "172.30.126.79",
avnapp_port : "8080",
template_file_location : "/var/lib/SessionSimulator/template",
macaddress_file_location : "/var/lib/SessionSimulator/mac",
asset_file_location : "/var/lib/SessionSimulator/asset",
report_file_location : "/var/lib/SessionSimulator/stats",
url_create_job : "/1/create/newJob",
url_show_job : "/1/status/job/",
url_stop_job : "/1/stop/",
url_engine_status : "/1/status/engine",
avn_gateway: ["172.30.124.33:13822","172.30.124.34:13822","172.30.111.13:13822","mdms-a-dsmcc.sc.g.charterlab.com:13822","96.34.182.138:13822","172.30.124.39:13822"],
process_lscp: true,
headend : ["ctec_a3h1","ctec_a3h2"],
system_version : "00",
system_protocol : "01"
}

