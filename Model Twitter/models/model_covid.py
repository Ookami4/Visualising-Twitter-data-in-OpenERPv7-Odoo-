from openerp.osv import osv,fields
import openerp

class model_covid(osv.osv):
    _name="twitter.covid"
    _columns={
        'tweet':fields.char("Tweet",required=True),
        'polarite':fields.float("Polarite",required=True)
    }
    def create(self, cr, uid, values, context=None):
        out=super(model_covid, self).create(cr, uid, values, context=context)
        self.pool.get("twitter.covidstatistic").create(cr, uid, {}, context=context)
        return out
    def write(self, cr, uid,ids, values, context=None):
        out=super(model_covid, self).write(cr, uid,ids, values, context=context)
        self.pool.get("twitter.covidstatistic").create(cr, uid, {}, context=context)
        return out
    def unlink(self, cr, uid, values, context=None):
        out=super(model_covid, self).unlink(cr, uid, values, context=context)
        self.pool.get("twitter.covidstatistic").create(cr, uid, {}, context=context)
        return out
model_covid()