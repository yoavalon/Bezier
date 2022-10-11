d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)

d.end()
