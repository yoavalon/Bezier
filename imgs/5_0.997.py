d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.position_pen(1,0)

d.end()
