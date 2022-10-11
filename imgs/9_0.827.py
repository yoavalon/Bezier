d = DslBezier()

d.position_pen(1,0)
d.position_pen(0,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
