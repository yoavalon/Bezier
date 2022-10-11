d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(0,3)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)

d.end()
