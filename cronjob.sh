datafolder="public/data"
datekawal=$(date +%Y-%m-%d_%H.%M)
filekawal="${datafolder}/kawal_${datekawal}"
scrapy crawl pilpreskawal -o "${filekawal}.xlsx"
datekpu=$(date +%Y-%m-%d_%H.%M)
filekpu="${datafolder}/kpu_${datekpu}"
scrapy crawl pilpres -o "${filekpu}.xlsx"
python excel_to_csv.py ${filekpu} ${filekawal}
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "truncate pilpres_kawal"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "\copy pilpres_kawal FROM '${PWD}/${filekawal}.csv' delimiter '|' csv header QUOTE E'\b' NULL AS '';"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "truncate pilpres_kpu"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "\copy pilpres_kpu FROM '${PWD}/${filekpu}.csv' delimiter '|' csv header QUOTE E'\b' NULL AS '';"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "REFRESH MATERIALIZED VIEW m_kawal;"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "REFRESH MATERIALIZED VIEW m_kpu;"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "REFRESH MATERIALIZED VIEW m_kpu_vs_kawal;"
psql -h 127.0.0.1 -w -U postgres -d pemilu -c "\copy (SELECT json_agg(m_kpu_vs_kawal) FROM m_kpu_vs_kawal) To '${PWD}/${datafolder}/komparasi_${datekpu}.json'"
sed -i 's/\\n//g' "${PWD}/${datafolder}/komparasi_${datekpu}.json"
ls "${datafolder}" > "${datafolder}/file_list.txt"
git add "${datafolder}"
git commit -m "update data ${datekpu}"
git push origin