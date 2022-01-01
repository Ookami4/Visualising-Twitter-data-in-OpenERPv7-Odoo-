from openerp.osv import osv,fields
import openerp

class model_omicron(osv.osv):
    _name="twitter.omicron"
    _columns={
        'tweet':fields.char("Tweet",required=True),
        'polarite':fields.float("Polarite",required=True)
    }
    def create(self, cr, uid, values, context=None):
        out=super(model_omicron, self).create(cr, uid, values, context=context)
        self.pool.get("twitter.omicronstatistic").create(cr, uid, {}, context=context)
        return out
    def write(self, cr, uid,ids, values, context=None):
        out=super(model_omicron, self).write(cr, uid,ids, values, context=context)
        self.pool.get("twitter.omicronstatistic").create(cr, uid, {}, context=context)
        return out
    def unlink(self, cr, uid, values, context=None):
        out=super(model_omicron, self).unlink(cr, uid, values, context=context)
        self.pool.get("twitter.omicronstatistic").create(cr, uid, {}, context=context)
        return out
model_omicron()