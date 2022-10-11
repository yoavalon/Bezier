d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(1,0)
d.straight_line(Direction.S, Length.medium)

d.end()
