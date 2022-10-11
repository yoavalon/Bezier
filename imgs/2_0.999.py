d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(2,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
