d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.position_pen(3,0)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)

d.end()
