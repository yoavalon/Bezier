d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)

d.end()
