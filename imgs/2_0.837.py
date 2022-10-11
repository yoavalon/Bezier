d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)

d.end()
